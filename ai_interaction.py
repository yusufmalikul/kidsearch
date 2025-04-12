# ai_interaction.py
import os
import requests
import json

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
# Using gemini-flash-1.5 as discussed, ensure this model is available/suitable on OpenRouter
MODEL_NAME = "google/gemini-pro-2.5"

def get_ai_response(query: str) -> str:
    """
    Gets a response from the configured OpenRouter model for the given query,
    applying safety and simplicity constraints via the prompt.

    Args:
        query: The user's search query.

    Returns:
        The AI-generated response text.

    Raises:
        ValueError: If the API key is not configured.
        requests.exceptions.RequestException: If the API request fails.
        KeyError: If the response format is unexpected.
    """
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY environment variable not set.")

    # Construct the detailed prompt
    prompt_instructions = """You are a helpful, friendly, and very safe assistant for children aged 6-10.
Your goal is to answer the user's query accurately but simply.
Follow these rules STRICTLY:
1.  Use simple words suitable for a 2nd-grade reading level (like explaining to a 7-year-old).
2.  Keep sentences very short, ideally under 10-12 words.
3.  Use concrete examples or simple analogies children can easily understand if possible.
4.  Maintain a positive, encouraging, and cheerful tone.
5.  ABSOLUTELY DO NOT discuss topics like violence, death, scary things (monsters, ghosts), weapons, politics, religion, complex adult relationships, drugs, or anything potentially upsetting or inappropriate for young children.
6.  If the user asks about a forbidden topic or the query seems unsafe, DO NOT answer the question. Instead, respond ONLY with: "I can't answer that, let's try a different question!"
7.  Provide concise answers. Get straight to the point.
8.  Do not ask follow-up questions. Just provide the answer.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": prompt_instructions},
            {"role": "user", "content": query}
        ]
        # Add other parameters like temperature, max_tokens if needed
        # "temperature": 0.6,
        # "max_tokens": 150,
    }

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            data=json.dumps(payload),
            timeout=30 # Add a timeout
        )
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        response_data = response.json()

        # Extract the content from the response structure
        # This structure might vary slightly based on OpenRouter/model specifics
        if response_data.get("choices") and len(response_data["choices"]) > 0:
            message = response_data["choices"][0].get("message")
            if message and message.get("content"):
                return message["content"].strip()
            else:
                raise KeyError("Could not find 'content' in response message.")
        else:
            raise KeyError("Response format unexpected, 'choices' not found or empty.")

    except requests.exceptions.RequestException as e:
        print(f"Error calling OpenRouter API: {e}")
        raise # Re-raise the exception to be handled by the caller
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing OpenRouter response: {e}")
        print(f"Raw response data: {response.text if 'response' in locals() else 'N/A'}")
        raise KeyError(f"Failed to parse AI response: {e}") # Raise a specific error type
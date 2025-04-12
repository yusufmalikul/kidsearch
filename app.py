from flask import Flask, render_template, request, jsonify
import requests # For catching request exceptions
import safety_filter
import ai_interaction

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main search page."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handles the search query."""
    query = request.json.get('query', '')
    if not query:
        return jsonify({'answer': "Please type something to search!"})

    print(f"Received query: {query}")

    # 1. Input Safety Check
    if not safety_filter.check_input_safety(query):
        print("Input safety check failed.")
        return jsonify({'answer': safety_filter.get_safe_fallback_message()})

    # 2. Get AI Response
    try:
        ai_response = ai_interaction.get_ai_response(query)
        print(f"AI Response received: {ai_response[:100]}...") # Log snippet

        # 3. Output Safety Check
        if not safety_filter.check_output_safety(ai_response):
            print("Output safety check failed.")
            return jsonify({'answer': safety_filter.get_safe_fallback_message()})

        # 4. Return safe AI response
        return jsonify({'answer': ai_response})

    except ValueError as e: # Handles missing API key
        print(f"Configuration error: {e}")
        return jsonify({'answer': "Sorry, there's a configuration problem."}), 500
    except (requests.exceptions.RequestException, KeyError, TimeoutError) as e:
        print(f"AI interaction error: {e}")
        return jsonify({'answer': "Oops! I couldn't get an answer right now. Try again?"}), 503 # Service Unavailable
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return jsonify({'answer': "Something went wrong on our side."}), 500

if __name__ == '__main__':
    # Note: Use a proper WSGI server for production
    app.run(debug=True)
# safety_filter.py

# Basic list of words/phrases to block. This should be expanded significantly.
# Consider using external libraries or more sophisticated methods for production.
BLOCKLIST = {
    # Obvious bad words (examples, not exhaustive)
    "damn", "hell", "stupid",
    # Topics to avoid
    "kill", "die", "death", "gun", "weapon", "violence",
    "scary monster", "ghost", "horror",
    # Potentially sensitive/complex topics
    "politics", "religion", "war", "sex", "drugs",
}

# A simple allowlist for testing might be useful too, but focus on blocking first.

def check_input_safety(query: str) -> bool:
    """
    Checks if the input query contains any blocked terms.
    Returns True if safe, False if unsafe.
    """
    query_lower = query.lower()
    for blocked_term in BLOCKLIST:
        if blocked_term in query_lower:
            print(f"Input safety check failed: Found '{blocked_term}' in query.")
            return False
    return True

def check_output_safety(response_text: str) -> bool:
    """
    Checks if the AI-generated response contains any blocked terms.
    Returns True if safe, False if unsafe.
    """
    response_lower = response_text.lower()
    for blocked_term in BLOCKLIST:
        if blocked_term in response_lower:
            print(f"Output safety check failed: Found '{blocked_term}' in response.")
            return False
    # TODO: Add checks for complexity, sentence length, etc. if needed.
    return True

def get_safe_fallback_message() -> str:
    """Returns a generic safe message for inappropriate queries or responses."""
    return "I can't answer that, let's try a different question!"
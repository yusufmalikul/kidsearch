# KidSearch AI

A simple, safe AI-powered search engine prototype designed for children aged 6-10.

## Description

This project provides a web interface where children can ask questions. The backend, built with Python and Flask, takes the query, performs basic safety checks, and then uses the OpenRouter API (specifically configured for `google/gemini-pro-2.5` in this implementation) with carefully crafted prompts to generate simple, safe, and age-appropriate answers.

The focus is on:
*   **Safety:** Basic input/output filtering and strict AI prompting to avoid inappropriate content.
*   **Simplicity:** Generating answers using vocabulary and sentence structures suitable for early elementary readers.

## Technology Stack

*   **Backend:** Python 3.11+, Flask
*   **AI Interaction:** OpenRouter API (`google/gemini-pro-2.5` model) via `requests` library
*   **Frontend:** HTML, CSS, JavaScript
*   **Environment:** Python Virtual Environment (`venv`)

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone git@github.com:yusufmalikul/kidsearch.git
    cd kidsearch
    ```

2.  **Create a Python virtual environment:**
    ```bash
    python3.11 -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   Linux/macOS: `source .venv/bin/activate`
    *   Windows (Git Bash/WSL): `source .venv/Scripts/activate`
    *   Windows (CMD): `.venv\Scripts\activate.bat`
    *   Windows (PowerShell): `.venv\Scripts\Activate.ps1`

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set the OpenRouter API Key:**
    You need an API key from [OpenRouter](https://openrouter.ai/). Set it as an environment variable named `OPENROUTER_API_KEY`.
    *   **Option A (Environment Variable):**
        ```bash
        # Linux/macOS
        export OPENROUTER_API_KEY='your_openrouter_api_key_here'
        # Windows CMD
        set OPENROUTER_API_KEY=your_openrouter_api_key_here
        # Windows PowerShell
        $env:OPENROUTER_API_KEY='your_openrouter_api_key_here'
        ```
        *(You'll need to do this every time you open a new terminal session unless you add it to your shell profile)*
    *   **Option B (.env file):**
        Create a file named `.env` in the project root directory (`kid-search/`) with the following content:
        ```
        OPENROUTER_API_KEY=your_openrouter_api_key_here
        ```
        Then, install `python-dotenv`:
        ```bash
        pip install python-dotenv
        ```
        And uncomment/add the following lines near the top of `app.py`:
        ```python
        from dotenv import load_dotenv
        load_dotenv()
        ```
        *(The `.env` file is already included in `.gitignore`)*

## Running the Application

1.  Make sure your virtual environment is activated and the `OPENROUTER_API_KEY` is set (either as an environment variable or via `.env`).
2.  Run the Flask development server:
    ```bash
    python app.py
    # Or directly using the venv python if not activated:
    # .venv/bin/python app.py
    ```
3.  Open your web browser and navigate to `http://127.0.0.1:5000` (or the address shown in the terminal).

Enter a query in the input box and press Enter to get a response.
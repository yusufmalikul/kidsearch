// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const resultArea = document.getElementById('result-area');

    searchInput.addEventListener('keypress', async (event) => {
        if (event.key === 'Enter') {
            const query = searchInput.value.trim();
            if (query) {
                // Clear previous results and show loading state
                resultArea.innerHTML = '';
                resultArea.classList.add('loading');
                searchInput.disabled = true; // Disable input during search

                try {
                    const response = await fetch('/search', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ query: query }),
                    });

                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }

                    const data = await response.json();
                    resultArea.innerText = data.answer || 'Sorry, something went wrong.';

                } catch (error) {
                    console.error('Search error:', error);
                    resultArea.innerText = 'Oops! Could not get an answer. Please try again.';
                } finally {
                    // Remove loading state and re-enable input
                    resultArea.classList.remove('loading');
                    searchInput.disabled = false;
                    // Optional: Clear input after search
                    // searchInput.value = '';
                }
            } else {
                resultArea.innerText = 'Please type something to search!';
            }
        }
    });
});
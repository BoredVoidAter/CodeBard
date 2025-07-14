// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    const codeContributionForm = document.getElementById('code-contribution-form');
    const codeInput = document.getElementById('code-input');
    const codeDisplay = document.getElementById('code-display');
    const narrativeDisplay = document.getElementById('narrative-display');

    if (codeContributionForm) {
        codeContributionForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const storyId = window.location.pathname.split('/').pop(); // Assumes URL like /story/1
            const codeLine = codeInput.value;

            if (!codeLine.trim()) {
                alert('Please enter a code line.');
                return;
            }

            try {
                const response = await fetch(`/api/story/${storyId}/add_line`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ code: codeLine })
                });

                if (response.ok) {
                    const data = await response.json();
                    // Update the displayed code and narrative
                    codeDisplay.textContent += '\n' + data.new_code_line;
                    narrativeDisplay.textContent = data.new_narrative;
                    codeInput.value = ''; // Clear input
                } else {
                    const errorData = await response.json();
                    alert(`Error: ${errorData.message}`);
                }
            } catch (error) {
                console.error('Error adding code line:', error);
                alert('Failed to add code line. Please try again.');
            }
        });
    }
});

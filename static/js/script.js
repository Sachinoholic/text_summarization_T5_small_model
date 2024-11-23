document.getElementById('summarizeButton').addEventListener('click', () => {
    const articleText = document.getElementById('articleText').value;
    const summarizeButton = document.getElementById('summarizeButton');
    const timerDiv = document.getElementById('timer');
    let startTime = null;

    summarizeButton.classList.add('loading'); // Add loading class for animation
    timerDiv.innerText = 'Processing...';

    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: articleText })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById('output').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('output').innerText = data.summary;
        }
        summarizeButton.classList.remove('loading'); // Remove loading class
        timerDiv.innerText = ''; // Clear timer
    })
    .catch(error => {
        document.getElementById('output').innerText = `Error: ${error}`;
        summarizeButton.classList.remove('loading'); // Remove loading class
        timerDiv.innerText = ''; // Clear timer
    });
});

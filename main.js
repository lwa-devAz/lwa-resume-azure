// main.js

// The AI will update this URL dynamically once your cloud backend is live
const API_URL = 'https://lwa-resume-api-azure.thankfulgrass-2096adae.uksouth.azurecontainerapps.io'; 

async function updateVisitorCounter() {

    const counterElement = document.getElementById('counter');
    if (!counterElement) return;

    try {
        // Send a POST request to trigger the database increment action
        const response = await fetch(`${API_URL}/api/counter`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Inject the numeric value safely into your existing HTML placeholder
        counterElement.innerText = data.count;
    } catch (error) {
        console.error('Failed to retrieve or update the visitor counter:', error);
        counterElement.innerText = '1'; // Graceful fallback value
    }
}

// Ensure the DOM is fully interactive before running the function
document.addEventListener('DOMContentLoaded', updateVisitorCounter);

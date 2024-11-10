const form = document.getElementById('check-form');
const status = document.getElementById('status');

form.addEventListener('submit', function(event){
    console.log('Form is Submitted!');
    event.preventDefault();

    const url = document.getElementById('url').value.trim();
    console.log(`URL For Search: ${url}`);

    const urlPattern = /^(https?:\/\/)?[^\s\/]+\.[a-zA-Z]{2,}$/;

    if (!urlPattern.test(url)) {
        console.log("URL failed validation:", url);
        alert("Invalid URL format. Please include a top-level domain like .com, .org, etc.");
        document.getElementById('url').value = ''; // Clear the input
        return;
    }

    checkURL(url);
});

async function checkURL(url) {
        const response = await fetch(`/URL_liveness?url=${url}`);
        const data = await response.json();
        console.log("Response data:", data);

        if (data.status_code === 'LIVE') {
            status.textContent = "The URL is live.";
            status.style.color = "green";
        } else if (data.status_code === 'UNREACHABLE') {
            status.textContent = "The URL is unreachable.";
            status.style.color = "red";
        } else if (data.status_code === 'INVALID_FORMAT') {
            alert("Invalid URL format. Please include a top-level domain like .com, .org, etc.");
            document.getElementById('url').value = '';
            status.textContent = '';
        }
}

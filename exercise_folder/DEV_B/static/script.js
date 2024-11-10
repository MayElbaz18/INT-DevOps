const form = document.getElementById('check-form');
const status = document.getElementById('status');

form.addEventListener('submit', function(event){
    console.log('Form is Submitted!');
    event.preventDefault();
    const url = document.getElementById('url').value;
    console.log(`URL For Search: ${url}`);
    checkURL(url);
})

async function checkURL(url) {
    const response = await fetch(`/URL_liveness?url=${url}`);
    const data = await response.json();
    console.log(data);
    console.log(data.status_code);
    status.textContent = `URL Status code is: ${data.status_code}`;
}
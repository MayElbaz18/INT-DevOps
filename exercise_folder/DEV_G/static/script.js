const form = document.getElementById('count-form');
const count = document.getElementById('count');

form.addEventListener('submit', function(event){
    console.log('Feedback is Submitted!');
    event.preventDefault();
    const words = document.getElementById('words').value;
    console.log(`Words To Count: ${words}`);
    Counter(words);    
})

async function Counter(words) {
    const response = await fetch(`/count?words=${words}`);
    const data = await response.json();
    console.log(data);
    console.log(data.Number_Of_Words);
    count.textContent = `Total Words: ${data.Number_Of_Words}`
}
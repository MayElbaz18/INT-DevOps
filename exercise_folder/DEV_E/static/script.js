const form = document.getElementById('calc-form');
const  equal = document.getElementById('equal');

form.addEventListener('submit', function(event){
    console.log('Form is Submitted!');
    event.preventDefault();
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operation = document.getElementById('operation').value;
    console.log(`num1:${num1}, num2:${num2} to calculate`);
    Calculate(num1, num2, operation);
})

async function Calculate(num1, num2, operation) {
    const response = await fetch(`/calc?num1=${num1}&num2=${num2}&operation=${operation}`);
    const data = await response.json();
    console.log(data);
    console.log(data.Result);

    if (typeof data === 'string'){
        alert(data);
    }
    equal.textContent = `Result: ${data.Result}`;
}
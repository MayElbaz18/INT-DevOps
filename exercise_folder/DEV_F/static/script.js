const form = document.getElementById('feedb-form');
const success = document.getElementById('success');

form.addEventListener('submit', function(event){
    console.log('Feedback is Submitted!');
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const feedback = document.getElementById('feedback').value;
    console.log(`name:${name}, email:${email}, feedback:${feedback}`);
    Feedback(name, email, feedback);
})

async function Feedback(name, email, feedback) {
  const response = await fetch(`/feedback?name=${name}&email=${email}&feedback=${feedback}`);
  const data = await response.json();
  console.log(data);
  console.log(data.Success);
  
  if (response.status === 400 && data === 'All fields are requierd for feedback'){
    alert('All fields are requierd for feedback');
  }
  else if (response.status === 400 && data === 'Please enter a valid email'){
    alert('Please enter a valid email');
  }
  else if (response.ok){
    success.textContent = `Success: ${data.Success}`;
    success.style.color = 'green';
  }
}
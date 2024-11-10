const form = document.getElementById('convert-form');
const tempf = document.getElementById('tempf');

form.addEventListener('submit', function(event){
    console.log('Form is Submitted!');
    event.preventDefault();
    const temp = document.getElementById('temp').value;
    console.log(`TEMPARTURE TO Convert: ${temp}`);
    ConvertTemp(temp);
})

async function ConvertTemp(temp) {
    const response = await fetch(`/temp_convertor?temp=${temp}`);
    const data = await response.json();
    console.log(data);
    console.log(data.converted_temp);

    if (response.status === 400 && data === 'TEMPARTURE Is Missing!') {
        alert("TEMPARTURE Is Missing!")
    }
    else if (response.status === 400 && data === 'TEMPARTURE Most Be A Number!') {
        alert('TEMPARTURE Most Be A Number!')
    }
    else if (response.ok) {
        tempf.textContent = `Temperature in Fahrenheit: ${data.converted_temp}`;
    }  
    
}
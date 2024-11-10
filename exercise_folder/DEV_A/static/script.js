document.getElementById("DisplayTime").onclick = function() {

    fetch('/get_time')
        .then(response => response.json())
        .then(data => {
            document.getElementById("DisplayTime").textContent = data.time;
        })
};

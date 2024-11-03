$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        const searchTerm = $('.search').val(); // Get the value from the input field

        $.get('/get_movie', { search: searchTerm }, function(data) {
            // Clear previous results
            $('#movieList').empty();
            
            // Split data into lines and display in list
            const lines = data.split('\n');
            lines.forEach(line => {
                if (line.trim()) { // Check if line is not empty
                    $('#movieList').append(`<li>${line}</li>`); // Append each line as a list item
                }
            });

            // Show the results div with fade-in effect
            $('#result').css('opacity', '0').show().animate({ opacity: 1 }, 500); // Fade in
        }).fail(function() {
            $('#movieList').empty();
            $('#movieList').append('<li>Error fetching data.</li>'); // Handle any errors
            
           
            $('#result').css('opacity', '0').show().animate({ opacity: 1 }, 500); // Fade in
        });
    });

    // Close result button functionality
    $('#closeResult').on('click', function() {
        $('#result').fadeOut(500); 
        $('.search').val(''); 
    });
});

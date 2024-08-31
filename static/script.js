document.getElementById('prediction-form').addEventListener('submit', function(event) {
    // Hide previous error message
    var errorMessage = document.getElementById('error-message');
    errorMessage.style.display = 'none';
    
    // Get all input fields
    var inputs = document.querySelectorAll('input[type="text"]');
    
    // Check if any input is empty
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value.trim() === '') {
            // Show error message and prevent form submission
            errorMessage.style.display = 'block';
            event.preventDefault();
            return;
        }
    }
});
function resetPage() {
    location.reload();
}
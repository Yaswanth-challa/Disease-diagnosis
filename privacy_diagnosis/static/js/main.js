// Client-side JavaScript for privacy-preserving medical diagnosis app

document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const diagnosisForm = document.getElementById('diagnosis-form');
    
    if (diagnosisForm) {
        diagnosisForm.addEventListener('submit', function(event) {
            // Basic form validation
            const temperature = document.getElementById('temperature').value;
            const heartRate = document.getElementById('heart_rate').value;
            const bloodPressure = document.getElementById('blood_pressure').value;
            const oxygenLevel = document.getElementById('oxygen_level').value;
            
            let isValid = true;
            let errorMessage = '';
            
            // Validate temperature (36-42°C is normal range)
            if (temperature < 30 || temperature > 45) {
                errorMessage += 'Temperature must be between 30-45°C.\n';
                isValid = false;
            }
            
            // Validate heart rate (40-200 bpm is acceptable range)
            if (heartRate < 40 || heartRate > 200) {
                errorMessage += 'Heart rate must be between 40-200 BPM.\n';
                isValid = false;
            }
            
            // Validate oxygen level (should be between 0-100%)
            if (oxygenLevel < 0 || oxygenLevel > 100) {
                errorMessage += 'Oxygen level must be between 0-100%.\n';
                isValid = false;
            }
            
            // If there are validation errors, prevent form submission
            if (!isValid) {
                event.preventDefault();
                alert('Please correct the following errors:\n' + errorMessage);
            } else {
                // If valid, simulate local encryption
                console.log('Encrypting data locally before sending to the server...');
                
                // Note: In a real implementation, we would actually encrypt the data
                // here using a JavaScript encryption library before submission
            }
        });
    }
    
    // Simulate edge computing latency for educational purposes
    const resultBox = document.querySelector('.results-box');
    if (resultBox) {
        // Add loading indicator that shows for 1.5 seconds
        resultBox.style.opacity = '0.6';
        resultBox.innerHTML = '<div class="loading">Processing diagnosis on edge device...</div>' + resultBox.innerHTML;
        
        setTimeout(function() {
            resultBox.style.opacity = '1';
            document.querySelector('.loading').style.display = 'none';
        }, 1500);
    }
});
const video = document.getElementById('video');

function startQRCodeReader() {
    // Check if the browser supports getUserMedia
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert('Sorry, your browser does not support QR code scanning.');
        return;
    }

    // Start the video stream from the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;

            // Initialize the QR code scanner
            const html5QrCode = new Html5Qrcode('video');

            html5QrCode.start(
                // Callback function when a QR code is detected
                (qrCodeMessage) => {
                    alert(`QR code detected: ${qrCodeMessage}`);
                    html5QrCode.stop(); // Stop scanning after detection
                },
                // Callback function for errors during scanning
                (errorMessage) => {
                    alert(`QR code scanning error: ${errorMessage}`);
                },
                // Callback function for video stream failures
                (videoError) => {
                    alert(`Video stream error: ${videoError}`);
                }
            );
        })
        .catch(function(error) {
            alert(`Unable to access the webcam: ${error}`);
        });
}

// Start the QR code reader when the page is loaded
window.addEventListener('load', startQRCodeReader);
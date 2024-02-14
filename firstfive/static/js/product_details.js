document.addEventListener('DOMContentLoaded', function() {
    var currentImageIndex = 0;
    var images = document.querySelectorAll('.hidden-image');
    var mainImage = document.getElementById('main-image');
    var sizeOptions = document.querySelectorAll('.sizebox');
    
    // Load the first image into the main image element
    mainImage.src = images[currentImageIndex].src;

    // Toggle last preview image
    function prevImage() {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        mainImage.src = images[currentImageIndex].src;
    }

    // Toggle next preview image
    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        mainImage.src = images[currentImageIndex].src;
    }

    // Function to handle size selection
    function handleSizeSelection(event) {
        // Get the selected size
        var selectedSize = event.target.getAttribute('value');
        
        // Perform any action you want with the selected size
        console.log('Selected size:', selectedSize);
        
        // Remove 'selected' class from all size options
        sizeOptions.forEach(function(sizeOption) {
            sizeOption.classList.remove('selected');
        });

        // Add 'selected' class to the clicked size option
        event.target.classList.add('selected');
    }

    // Add event listeners to the buttons
    document.querySelector('.option-left').addEventListener('click', prevImage);
    document.querySelector('.option-right').addEventListener('click', nextImage);

    // Add event listeners to size options
    sizeOptions.forEach(function(sizeOption) {
        sizeOption.addEventListener('click', handleSizeSelection);
    });
});
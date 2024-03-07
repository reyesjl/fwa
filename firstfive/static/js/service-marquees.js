document.addEventListener("DOMContentLoaded", function() {
  // Function to start scrolling
  function startScrolling() {
    var marquee = document.querySelector('.marquees-list');
    marquee.scrollLeft += 1; // Adjust the speed by changing this value
  }

  // Start scrolling once the DOM is loaded
  var scrollInterval = setInterval(startScrolling, 30); // Adjust the interval for slower or faster scrolling
  
  // Pause scrolling when the user hovers
  var marqueeList = document.querySelector('.marquees-list');
  marqueeList.addEventListener('mouseover', function() {
    clearInterval(scrollInterval); // Slow scrolling
  });

  // Resume scrolling when the user stops hovering
  marqueeList.addEventListener('mouseout', function() {
    scrollInterval = setInterval(startScrolling, 30); // Restart scrolling
  });
});

// Function for random card styling
function randomCardStyling() {
  const itemCards = document.querySelectorAll('.scroller-platter.itemcard');

  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function applyStyles(element) {
    element.style.backgroundColor = 'black';
    element.style.color = 'white';
  }

  function randomStyling() {
    const numToStyle = getRandomInt(1, itemCards.length - 1);
    const styledIndices = [];

    for (let i = 0; i < numToStyle; i++) {
      let randomIndex;
      do {
        randomIndex = getRandomInt(0, itemCards.length - 1);
      } while (styledIndices.includes(randomIndex));
      applyStyles(itemCards[randomIndex]);
      styledIndices.push(randomIndex);
    }
  }

  randomStyling();
}

// Function to control category slider
function controlCategorySlider(direction) {
  const categorySlider = document.querySelector('.scroller-nav');
  const itemWidth = categorySlider.offsetWidth; // Width of the visible area
  const scrollAmount = itemWidth / 2; // Amount to scroll each time

  if (direction === 'left') {
    categorySlider.scrollLeft -= scrollAmount;
  } else {
    categorySlider.scrollLeft += scrollAmount;
  }
}

// Function to control product slider
function controlProductSlider(direction) {
  const productSlider = document.querySelector('.scroller-overflow');
  const itemWidth = productSlider.offsetWidth; // Width of the visible area
  const scrollAmount = itemWidth / 2; // Amount to scroll each time

  if (direction === 'left') {
    productSlider.scrollLeft -= scrollAmount;
  } else {
    productSlider.scrollLeft += scrollAmount;
  }
}

// Run functions when the document is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM loaded");

  // Execute random card styling
  randomCardStyling();

  // Event listeners for category slider buttons
  console.log("Adding event listeners for category slider buttons");
  document.querySelector('.scroller-button.left').addEventListener('click', function() {
    //console.log("Left button for category slider clicked");
    controlCategorySlider('left');
  });

  document.querySelector('.scroller-button.right').addEventListener('click', function() {
    //console.log("Right button for category slider clicked");
    controlCategorySlider('right');
  });

  // Event listeners for product slider buttons
  console.log("Adding event listeners for product slider buttons");
  document.querySelectorAll('.scroller-button.left')[1].addEventListener('click', function() {
    //console.log("Left button for product slider clicked");
    controlProductSlider('left');
  });

  document.querySelectorAll('.scroller-button.right')[1].addEventListener('click', function() {
    //console.log("Right button for product slider clicked");
    controlProductSlider('right');
  });
});

function randomCardStyling() {
  // Select all elements with class 'scroller-platter itemcard'
  const itemCards = document.querySelectorAll('.scroller-platter.itemcard');

  // Function to generate a random number within a range
  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  // Function to apply black background and white color to a given element
  function applyStyles(element) {
    element.style.backgroundColor = 'black';
    element.style.color = 'white';
  }

  // Function to randomly select and style elements
  function randomStyling() {
    // Choose a random number of elements to style (between 1 and the total number of item cards)
    const numToStyle = getRandomInt(1, itemCards.length);

    // Array to store indices of already styled elements to avoid repetition
    const styledIndices = [];

    // Style the randomly selected elements
    for (let i = 0; i < numToStyle; i++) {
      let randomIndex;

      // Ensure that we don't style the same element twice
      do {
        randomIndex = getRandomInt(0, itemCards.length - 1);
      } while (styledIndices.includes(randomIndex));

      applyStyles(itemCards[randomIndex]);
      styledIndices.push(randomIndex);
    }
  }

  // Call the randomStyling function to apply styles on load
  randomStyling();
}

// Run randomCardStyling function when the document is fully loaded
document.addEventListener('DOMContentLoaded', randomCardStyling);

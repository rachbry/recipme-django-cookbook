function toggleDescription() {
    var descriptionContainer = document.getElementById('recipeDescriptionContainer');
    var button = document.querySelector('.read-more-button');

    // Toggle the expanded class
    descriptionContainer.classList.toggle('expanded');

    // Check if there are only two lines of text
    var isTwoLines = descriptionContainer.scrollHeight <= descriptionContainer.clientHeight;

    // Update button text based on the current state
    button.textContent = descriptionContainer.classList.contains('expanded') ? 'See Less' : 'Read More';

    // If not expanded and there are only two lines, hide the button
    if (!descriptionContainer.classList.contains('expanded')) {
        button.style.display = isTwoLines ? 'none' : 'inline-block';
    } else {
        button.style.display = 'inline-block';
    }
}

function scrollRecipes(direction) {
    const container = document.querySelector('.overflow-auto');
    const scrollAmount = 200; // Adjust the scroll amount as needed

    if (direction === 'left') {
        container.scrollLeft -= scrollAmount;
    } else if (direction === 'right') {
        container.scrollLeft += scrollAmount;
    }
}
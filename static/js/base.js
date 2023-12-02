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
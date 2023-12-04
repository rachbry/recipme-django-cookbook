
function scrollRecipes(direction) {
    const container = document.querySelector('.overflow-auto');
    const scrollAmount = 200; // Adjust the scroll amount as needed

    if (direction === 'left') {
        container.scrollLeft -= scrollAmount;
    } else if (direction === 'right') {
        container.scrollLeft += scrollAmount;
    }
}
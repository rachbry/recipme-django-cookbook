// function scrollRecipes(direction) {
//     console.log('scrollRecipes function called');
//     const container = document.querySelector('.overflow-auto');
//     const scrollAmount = 400; // Adjust the scroll amount as needed

//     if (direction === 'left') {
//         container.scrollLeft -= scrollAmount;
//     } else if (direction === 'right') {
//         container.scrollLeft += scrollAmount;
//     }
// }


function filterCards(mealType) {
    // Hide all cards
    const cards = document.querySelectorAll('.recipe-cards .card');
    cards.forEach(card => {
        card.style.display = 'none';
    });

    // Show cards with the selected meal type
    const filteredCards = document.querySelectorAll(`.recipe-cards .${mealType}`);
    filteredCards.forEach(card => {
        card.style.display = 'block';
    });
}

function showAllCards() {
    // Show all cards
    const cards = document.querySelectorAll('.recipe-cards .card');
    cards.forEach(card => {
        card.style.display = 'block';
    });
}
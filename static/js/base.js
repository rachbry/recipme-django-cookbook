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


// function filterCards(mealType) {
//     // Hide all cards
//     const cards = document.querySelectorAll('.recipe-cards .card');
//     cards.forEach(card => {
//         card.style.display = 'none';
//     });

//     // Show cards with the selected meal type
//     const filteredCards = document.querySelectorAll(`.recipe-cards .${mealType}`);
//     filteredCards.forEach(card => {
//         card.style.display = 'block';
//     });
// }

// function showAllCards() {
//     // Show all cards
//     const cards = document.querySelectorAll('.recipe-cards .card');
//     cards.forEach(card => {
//         card.style.display = 'block';
//     });
// }

function toggleDescription() {
    var content = document.getElementById("content");
    var btn = document.getElementById("read-more-btn");

    // Toggle the visibility of the hidden content
    var hiddenContent = content.querySelector(".hidden-content");
    if (hiddenContent.style.display === "none" || hiddenContent.style.display === "") {
        hiddenContent.style.display = "block";
        btn.innerHTML = "Read Less";
    } else {
        hiddenContent.style.display = "none";
        btn.innerHTML = "Read More";
    }
}
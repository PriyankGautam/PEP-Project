document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("click", () => {
            card.style.background = "rgba(255,255,255,0.3)";
            card.style.transform = "scale(1.1)";
            setTimeout(() => {
                card.style.background = "rgba(255,255,255,0.1)";
                card.style.transform = "scale(1)";
            }, 500);
        });
    });
});

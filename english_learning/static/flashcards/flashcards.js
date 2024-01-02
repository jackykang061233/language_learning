// for (const frontOrBack of document.querySelectorAll('.flashcards-inner *')) {
//   frontOrBack.addEventListener('click', () => {
//     frontOrBack.parentElement.classList.toggle('flipped');
//   });
// }
const cards = document.querySelectorAll(".card");

function flipCard() {
  this.classList.toggle("flip");
}
cards.forEach((card) => card.addEventListener("click", flipCard));
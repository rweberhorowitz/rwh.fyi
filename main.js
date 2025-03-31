const audio = document.querySelector("audio");

const playButton = document.getElementById("play-button");
const pauseButton = document.getElementById("pause-button");

playButton.addEventListener("click", () => {
    audio.play();
});

pauseButton.addEventListener("click", () => {
    audio.pause();
});

function openModal(element) {
    var modal = document.getElementById('imageModal');
    var modalImg = document.getElementById('modalImage');
    modal.style.display = "block";
    modalImg.src = element.src;
}

function closeModal() {
    var modal = document.getElementById('imageModal');
    modal.style.display = "none";
}

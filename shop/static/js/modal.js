const modal = document.querySelector(".msg-modal");
const closeButton = document.querySelectorAll(".msg-modal-close");

const msgModalClose = () => {
  modal.classList.remove("fadeIn");
  modal.classList.add("fadeOut");
  setTimeout(() => {
    modal.style.display = "none";
  }, 500);
};

const openMsgModal = () => {
  modal.classList.remove("fadeOut");
  modal.classList.add("fadeIn");
  modal.style.display = "flex";
};

for (let i = 0; i < closeButton.length; i++) {
  const elements = closeButton[i];

  elements.onclick = (e) => msgModalClose();

  modal.style.display = "none";

  window.onclick = function (event) {
    if (event.target == modal) msgModalClose();
  };
}

let guideBtn = document.getElementById("guideBtn");
let driverBtn = document.getElementById("driverBtn");
let guideInput = document.querySelector(".forGuide");
let driverInput = document.querySelector(".forDriver");
let bus = document.querySelector(".busImage");
guideBtn.addEventListener("click", () => {
  if (driverBtn.classList.contains("selectedBtn")) {
    driverBtn.classList.remove("selectedBtn");
  }
  guideBtn.classList.add("selectedBtn");
  guideInput.classList.remove("none");
  driverInput.classList.add("none");
  bus.classList.remove("busActive");
});

driverBtn.addEventListener("click", () => {
  if (guideBtn.classList.contains("selectedBtn")) {
    guideBtn.classList.remove("selectedBtn");
  }
  driverBtn.classList.add("selectedBtn");
  guideInput.classList.add("none");
  driverInput.classList.remove("none");
  bus.classList.add("busActive");
});

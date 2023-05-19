let guideBtn = document.getElementById("guideBtn");
let driverBtn = document.getElementById("driverBtn");

guideBtn.addEventListener("click", () => {
  console.log("hello");
  if (driverBtn.classList.contains("selectedBtn")) {
    driverBtn.classList.remove("selectedBtn");
  }
  guideBtn.classList.add("selectedBtn");
});

driverBtn.addEventListener("click", () => {
  if (guideBtn.classList.contains("selectedBtn")) {
    guideBtn.classList.remove("selectedBtn");
  }
  driverBtn.classList.add("selectedBtn");
});

let a = [1, 2, 3, 4, 5];
console.log(a);

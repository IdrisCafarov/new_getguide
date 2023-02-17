let guideBtn = document.querySelector(".guideBtn");
let companyBtn = document.querySelector(".companyBtn");
let guideSide = document.querySelector(".guideSide");
let companySide = document.querySelector(".companySide");

guideBtn.addEventListener("click", () => {
  guideBtn.classList.add("activeBtn");
  companyBtn.classList.remove("activeBtn");
  companySide.classList.add("hide");
  guideSide.classList.remove("hide");
});

companyBtn.addEventListener("click", () => {
  companyBtn.classList.add("activeBtn");
  guideBtn.classList.remove("activeBtn");
  companySide.classList.remove("hide");
  guideSide.classList.add("hide");
});

// Giudes Filters
const filterHeader = document.querySelectorAll(".filterHeader");
filterHeader.forEach((e) => {
  e.addEventListener("click", () => {
    e.nextElementSibling.classList.toggle("dropdownHeight");
    e.lastElementChild.classList.toggle("rotate180");
  });
});

// Guide Filetrs End

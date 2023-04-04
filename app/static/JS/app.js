const icons = document.querySelectorAll(".fa-plus");
const answer = document.querySelectorAll(".faq-answer");

[...icons].map((i) => {
  i.addEventListener("click", (e) => {
    icons.forEach((a) => a.classList.remove("rotate"));
    i.classList.add("rotate");
    [...document.querySelectorAll(".faq-answer")].map(
      (a) => (a.style.height = 0)
    );
    let p = e.target.nextElementSibling;
    p.style.height = `${p.scrollHeight}px`;
  });
});


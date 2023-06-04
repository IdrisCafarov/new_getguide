let personalInfo = document.querySelector(".personalInfo");
let calendarPage = document.querySelector(".calendarPage");
let notificationPage = document.querySelector(".notificationPage");

let profIcon = document.getElementById("profIcon");
let calendarIcon = document.getElementById("calendarIcon");
let notIcon = document.getElementById("notIcon");

profIcon.addEventListener("click", () => {
  profIcon.classList.add("activeIcon");
  calendarIcon.classList.remove("activeIcon");
  notIcon.classList.remove("activeIcon");
  personalInfo.classList.remove("none");
  calendarPage.classList.add("none");
  notificationPage.classList.add("none");
});

calendarIcon.addEventListener("click", () => {
  calendarIcon.classList.add("activeIcon");
  profIcon.classList.remove("activeIcon");
  notIcon.classList.remove("activeIcon");
  personalInfo.classList.add("none");
  calendarPage.classList.remove("none");
  notificationPage.classList.add("none");
});

notIcon.addEventListener("click", () => {
  calendarIcon.classList.remove("activeIcon");
  profIcon.classList.remove("activeIcon");
  notIcon.classList.add("activeIcon");
  personalInfo.classList.add("none");
  calendarPage.classList.add("none");
  notificationPage.classList.remove("none");
});

let oneNotification = document.querySelectorAll(".notificationLeft .not");
let displayNotification = document.querySelector(".rightBody p");
oneNotification.forEach((e) => {
  if (e.classList.contains("activeNotification")) {
    displayNotification.textContent = e.firstElementChild.textContent;
  }
  e.addEventListener("click", () => {
    [...oneNotification].map((a) => {
      a.classList.remove("activeNotification");
    });
    e.classList.add("activeNotification");
    displayNotification.textContent = e.firstElementChild.textContent;
  });
});

// personal info and profile
let firstProfile = document.querySelector(".firstProfile");
let secondProfile = document.querySelector(".secondProfile");
let infoSide = document.getElementById("infoSide");
let profileSide = document.getElementById("profileSide");
let accessSides = document.querySelectorAll(".profileHeaderTop p");
[...accessSides].map((p) => {
  p.addEventListener("click", (e) => {
    [...accessSides].forEach((a) => {
      if (a.classList.contains("prHeadActive")) {
        a.classList.remove("prHeadActive");
      }
    });
    e.target.classList.add("prHeadActive");
    // Show & Hide Sides
    if (infoSide.classList.contains("prHeadActive")) {
      secondProfile.classList.add("none");
      firstProfile.classList.remove("none");
    } else if (profileSide.classList.contains("prHeadActive")) {
      secondProfile.classList.remove("none");
      firstProfile.classList.add("none");
    }
  });
});

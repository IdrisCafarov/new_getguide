const addBusyDate = () => {
  fetch("http://localhost:8000/add_busy_date/")
    .then((res) => res.json())
    .then((res) => console.log(res));
};
// addBusyDate();

// let busy_arr;
const showBusyDate = () => {
  fetch("http://localhost:8000/show_busy_date/")
    .then((res) => res.json())
    .then((res) => console.log(res));
};
showBusyDate();

let user_id = 1;
let busy_arr = [
  {
    id: 1,
    dates: ["20 April 2023", "21 February 2023", "4 May 2023"],
  },
  {
    id: 2,
    dates: ["25 April 2023", "27 February 2023"],
  },
];

let busy = busy_arr.find((e) => e.id == user_id);

const isLeapYear = (year) => {
  return (
    (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
    (year % 100 === 0 && year % 400 === 0)
  );
};
const getFebDays = (year) => {
  return isLeapYear(year) ? 29 : 28;
};
let calendar = document.querySelector(".calendar");
const month_names = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
let month_picker = document.querySelector("#month-picker");
const dayTextFormate = document.querySelector(".day-text-formate");
const timeFormate = document.querySelector(".time-formate");
const dateFormate = document.querySelector(".date-formate");

month_picker.onclick = () => {
  month_list.classList.remove("hideonce");
  month_list.classList.remove("hide");
  month_list.classList.add("show");
  dayTextFormate.classList.remove("showtime");
  dayTextFormate.classList.add("hidetime");
  timeFormate.classList.remove("showtime");
  timeFormate.classList.add("hideTime");
  dateFormate.classList.remove("showtime");
  dateFormate.classList.add("hideTime");
};

const generateCalendar = (month, year) => {
  let calendar_days = document.querySelector(".calendar-days");
  calendar_days.innerHTML = "";
  let calendar_header_year = document.querySelector("#year");
  let days_of_month = [
    31,
    getFebDays(year),
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
  ];

  let currentDate = new Date();
  console.log(currentDate);
  // console.log(currentDate.getDate());
  month_picker.innerHTML = month_names[month];

  calendar_header_year.innerHTML = year;

  let first_day = new Date(year, month);

  for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {
    let day = document.createElement("div");

    if (i >= first_day.getDay()) {
      day.innerHTML = i - first_day.getDay() + 1;
      busy.dates.map((e) => {
        let busy_day = e.split(" ")[0];
        let busy_month = e.split(" ")[1];
        let busy_year = e.split(" ")[2];
        if (
          document.getElementById("month-picker").innerText === busy_month &&
          document.getElementById("year").innerText === busy_year &&
          day.innerHTML === busy_day
        ) {
          day.classList.add("busy-date");
        }
      });

      if (
        i - first_day.getDay() + 1 === currentDate.getDate() &&
        year === currentDate.getFullYear() &&
        month === currentDate.getMonth()
      ) {
        day.classList.add("current-date");
      }
    }
    calendar_days.appendChild(day);
    day.addEventListener("click", (e) => {
      let selectedMonth = document.getElementById("month-picker").innerText;
      let selectedDay = day.innerText;
      let selectedYear = document.getElementById("year").innerText;
      const selectedDate = new Date(
        `${selectedMonth} ${selectedDay} ${selectedYear}`
      );
      console.log(selectedDate);
      // FETCH DATE TO API
      fetch("http://localhost:8000/add_busy_date/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user: 4,
          date: `${selectedYear}-07-${selectedDay}`
          ,
        }),
      })
        .then((response) => response.json())
        .then((response) => console.log(JSON.stringify(response)))
        .catch((error) => console.error(error));
    });
  }
};

let month_list = calendar.querySelector(".month-list");
month_names.forEach((e, index) => {
  let month = document.createElement("div");
  month.innerHTML = `<div>${e}</div>`;

  month_list.append(month);
  month.onclick = () => {
    currentMonth.value = index;
    generateCalendar(currentMonth.value, currentYear.value);
    month_list.classList.replace("show", "hide");
    dayTextFormate.classList.remove("hideTime");
    dayTextFormate.classList.add("showtime");
    timeFormate.classList.remove("hideTime");
    timeFormate.classList.add("showtime");
    dateFormate.classList.remove("hideTime");
    dateFormate.classList.add("showtime");
  };
});

(function () {
  month_list.classList.add("hideonce");
})();
document.querySelector("#pre-year").onclick = () => {
  --currentYear.value;
  generateCalendar(currentMonth.value, currentYear.value);
};
document.querySelector("#next-year").onclick = () => {
  ++currentYear.value;
  generateCalendar(currentMonth.value, currentYear.value);
};

let currentDate = new Date();
let currentMonth = { value: currentDate.getMonth() };
let currentYear = { value: currentDate.getFullYear() };
generateCalendar(currentMonth.value, currentYear.value);

const todayShowTime = document.querySelector(".time-formate");
const todayShowDate = document.querySelector(".date-formate");

const currshowDate = new Date();
const showCurrentDateOption = {
  year: "numeric",
  month: "long",
  day: "numeric",
  weekday: "long",
};
const currentDateFormate = new Intl.DateTimeFormat(
  "en-US",
  showCurrentDateOption
).format(currshowDate);
todayShowDate.textContent = currentDateFormate;
setInterval(() => {
  const timer = new Date();
  const option = {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
  };
  const formateTimer = new Intl.DateTimeFormat("en-us", option).format(timer);
  let time = `${`${timer.getHours()}`.padStart(
    2,
    "0"
  )}:${`${timer.getMinutes()}`.padStart(
    2,
    "0"
  )}: ${`${timer.getSeconds()}`.padStart(2, "0")}`;
  todayShowTime.textContent = formateTimer;
}, 1000);

// ---------------API---------------

// -------------------------
// -------CUSTOMIZE---------
// -------------------------
// let modal = document.querySelector(".calendar .modal");
// let yes = document.getElementById("yes");
// let oneDay = document.querySelectorAll(".calendar-days div");
// let closeBtn = document.querySelector(".modal .close");
// let selectedDay = [];
// oneDay.forEach((d) => {
//   d.addEventListener("click", (e) => {
//     // console.log(selectedDay.length);
//     if (e.target.classList.contains("disabled")) {
//       let question = confirm(
//         "Today is selected as busy. Do you want to delete?"
//       );
//       if (question == true) {
//         selectedDay = selectedDay.filter((item) => item !== e.target);
//         e.target.classList.remove("disabled");
//       }
//     } else {
//       let response = confirm("Have a busy day?");
//       if (response == true) {
//         selectedDay.push(e.target);
//       } else {
//         return;
//       }
//     }

//     [...selectedDay].map((a) => {
//       a.classList.add("disabled");
//     });
//   });
// });

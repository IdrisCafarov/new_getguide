let calendar = document.querySelector(".calendar");
let month_picker = document.querySelector("#month-picker");
const dayTextFormate = document.querySelector(".day-text-formate");
const timeFormate = document.querySelector(".time-formate");
const dateFormate = document.querySelector(".date-formate");
let month_list = calendar.querySelector(".month-list");
let modal = document.querySelector(".modal");
let yes = document.querySelector("#yes");

let currentDate = new Date();
let currentMonth = { value: currentDate.getMonth() };
let currentYear = { value: currentDate.getFullYear() };

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

const isLeapYear = (year) => {
  return (
    (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
    (year % 100 === 0 && year % 400 === 0)
  );
};

const getFebDays = (year) => {
  return isLeapYear(year) ? 29 : 28;
};

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

function getCsrfToken() {
  const csrfTokenElement = document.querySelector('meta[name="csrf-token"]');
  return csrfTokenElement ? csrfTokenElement.content : "";
}

const showBusyDate = async () => {
  await fetch("http://localhost:8000/show_busy_date/")
    .then((res) => res.json())
    .then((res) => {
      let arr = [];
      let user = res.find((e) => e.id == user_id);
      user.dates.map((e) => arr.push(e.date));
      calendar_funk(arr);
    });
};
showBusyDate();

const calendar_funk = (busy) => {
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
    month_picker.innerHTML = month_names[month];

    calendar_header_year.innerHTML = year;

    let first_day = new Date(year, month);

    for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {
      let day = document.createElement("div");

      if (i >= first_day.getDay()) {
        day.innerHTML = i - first_day.getDay() + 1;
      }
      calendar_days.appendChild(day);
      busy.map((e) => {
        let busy_day = e.split("-")[2].replace("0", "");
        let busy_month = Number(e.split("-")[1].replace("0", "")) - 1;
        let busy_year = e.split("-")[0];
        if (
          month_names[busy_month] ===
            document.getElementById("month-picker").innerText &&
          document.getElementById("year").innerText === busy_year &&
          day.innerHTML === busy_day.replace("0", "")
        ) {
          day.classList.add("busy-date");
        }
      });
      day.setAttribute("onclick", "send_data_api(this)");
    }
  };
  month_list.innerHTML = "";
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
};

const send_data_api = (day) => {
  modal.classList.add("showModal");
  yes.addEventListener("click", () => {
    let selectedMonth = document.getElementById("month-picker").innerText;
    let selectedDay = day.innerText;
    let selectedYear = document.getElementById("year").innerText;
    let monthIndex = month_names.indexOf(selectedMonth) + 1;
    monthIndex < 10 ? (monthIndex = "0" + monthIndex) : monthIndex;
    const selectedDate = new Date(
      `${selectedMonth} ${selectedDay} ${selectedYear}`
    );
    // AJAX
    $.ajax({
      url: "http://localhost:8000/add_busy_date/",
      type: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(),
      },
      data: JSON.stringify({
        user: user_id,
        date: `${selectedYear}-${monthIndex}-${selectedDay}`,
      }),
      success: function (response) {
        showBusyDate();
        modal.classList.remove("showModal");
      },

      error: function (xhr) {
        console.log(xhr);
      },
    });
  });
};

const close_modal = () => {
  modal.classList.remove("showModal");
};

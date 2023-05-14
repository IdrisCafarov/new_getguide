let guide = document.getElementById("guide");
let company = document.getElementById("company");
let driver = document.getElementById("driver");
guide?.addEventListener("click", () => {
  guide.checked = true;
  company.checked = false;
  company.required = false;
  driver.checked = false;
  driver.required= false;

  // document.getElementById("reqSpan").style.display = "none";
  // document.getElementById("signBtn").disabled = false;
});
company?.addEventListener("click", () => {
  company.checked = true;
  guide.checked = false;
  guide.required = false;
  driver.checked = false;
  driver.required = false;

  // document.getElementById("reqSpan").style.display = "none";
  // document.getElementById("signBtn").disabled = false;
});
driver?.addEventListener("click", () => {
  driver.checked = true;
  guide.checked = false;
  guide.required = false;
  company.checked = false;
  company.required = false;

  // document.getElementById("reqSpan").style.display = "none";
  // document.getElementById("signBtn").disabled = false;
});


// $(document).ready(function(){
//   var checkboxes = $('.checkboxes');
//   checkboxes.change(function(){
//       if($('.checkboxes:checked').length>0) {
//           checkboxes.removeAttr('required');
//       } else {
//           checkboxes.attr('required', 'required');
//       }
//   });
// });
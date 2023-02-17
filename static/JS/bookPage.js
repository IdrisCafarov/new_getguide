$(".infoHeader").click(function () {
  $(".infoResponse").slideUp(400);
  $(this).find(".infoResponse").slideDown(500);
  $(".rotate180").removeClass("rotate180");
  $(this).find("i").addClass("rotate180");
});

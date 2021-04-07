// function openNav() {
//   document.getElementById("mySidenav").style.width = "250px";
//   document.getElementById("main").style.marginLeft = "250px";
// }
// function myFunction(x) {
//   x.classList.toggle("change");
// }
$(document).ready(function() {
  $("#open").click(function(){
    $("#mySidenav").css("width","250px");
    $("#main_content").addClass("attendanceNavWhileOpen");
    $("#main_content").removeClass("attendanceNavWhileClose");
  });
  $("#close").click(function(){
    $("#mySidenav").css("width","0");
    $("#main").css("margin-left","0");
    $('.active').attr("aria-expanded","false");
    $("#hrdrop").removeClass("show");
    $("#navigation").css('margin-left','0px');
    $("#main_content").addClass("attendanceNavWhileClose");
    $("#main_content").removeClass("attendanceNavWhileOpen");
  });
  $("#hrdrop").click(function(){
    $("#dropdown").css('display','block');
    $("#dropdown").css('background-color','black');
    $("#dropdown").css('color','white');
  });
  $("#Attendance").click(function(){

    // $("#main_content").load($("#Attendance").data('url'));
    //
    // alert($("#Attendance").data('url'));
    $('#Attendance').attr("href",$("#Attendance").data('url'));
    $.ajax({
      url:$("#Attendance").data('url'),
      type:'html',
      success:function(){

      }

    });
  });
});

// function closeNav() {
//   document.getElementById("mySidenav").style.width = "0";
//   document.getElementById("main").style.marginLeft= "0";
// }

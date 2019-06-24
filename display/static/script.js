$(document).ready(function() {
  var datealert = $('.datealert');
  datealert.each(function(index){
    var today = new Date();
    var compareyear = "20"+$(this).text().split('/')[1];
    var comparemonth;
    if ($(this).text().split('/')[0].length < 2) {
      if ($(this).text().split('/')[0] == '9') {
        comparemonth = "10";
      } else {
        comparemonth = "0" + (parseInt($(this).text().split('/')[0]) + 1);
      }
    } else {
      if(parseInt($(this).text().split('/')[0]) == '12'){
        comparemonth = parseInt($(this).text().split('/')[0]);

      } else {
        comparemonth = parseInt($(this).text().split('/')[0]) + 1;

      }
    }
    var comparedate = new Date(compareyear+"-"+comparemonth);

    if (today < comparedate) {
      if (today.getYear() == comparedate.getYear()){
        if (today.getMonth() == comparedate.getMonth()) {
          $(this).css('background-color', 'yellow');
          $(this).css('color', 'black');
        }
      }
    } else {
      $(this).css('background-color', 'red');
    }
  });
  var tachalert = $('.tachalert');
  tachalert.each(function(index){
    var duetime = parseFloat($(this).text());
    // console.log(duetime);
    var tachtime = parseFloat($('#tachtime'+$(this).data('id')).text());
    // console.log(tachtime);
    if (duetime >= tachtime) {
      if (tachtime + 10.0 >= duetime) {
        $(this).css('background-color', 'yellow');
        $(this).css('color', 'black');
      }
    } else {
      $(this).css('background-color', 'red');
    }
  });

});


function changecolor() {
  displaytime()
  var datetd = document.getElementsByClassName("pilotdatetd");
  var currentdate = new Date();
  var currentmonthlastday = new Date(currentdate.getFullYear(), currentdate.getMonth() + 1, 0);
  // See if str date is greater than the end of this month plus one
  for (i = 0; i < datetd.length; i++) {
    // console.log(datetd.item(i).innerHTML);
    var str = datetd.item(i).innerHTML.split("/");
    str[1] = "20" + str[1]
    // console.log(str[1]);
    var strdate = new Date(str[1], str[0]);
    var strdateendofmonth = new Date(strdate.getFullYear(), strdate.getMonth(), 0);
    // console.log(endofmonth);
    if (strdateendofmonth.getFullYear() == currentmonthlastday.getFullYear() && strdateendofmonth.getMonth() == currentmonthlastday.getMonth()) {
      datetd.item(i).style.backgroundColor = "yellow";
      datetd.item(i).style.color = "black";
    } else if (strdateendofmonth.getFullYear() == currentmonthlastday.getFullYear() && strdateendofmonth.getMonth() == currentmonthlastday.getMonth() + 1) {

      datetd.item(i).style.backgroundColor = "yellow";
      datetd.item(i).style.color = "black";
    } else if (strdateendofmonth.getFullYear() == currentmonthlastday.getFullYear() && strdateendofmonth.getMonth() < currentmonthlastday.getMonth()) {
      datetd.item(i).style.backgroundColor = "red";
      datetd.item(i).style.color = "black";
    }
  }

  var gracedatetd = document.getElementsByClassName("gracepilotdatetd");

  for (i = 0; i < gracedatetd.length; i++) {
    var str = gracedatetd.item(i).innerHTML.split("/");
    str[1] = "20" + str[1]
    // console.log(str[1]);
    var strdate = new Date(str[1], str[0]);
    var strdateendofmonth = new Date(strdate.getFullYear(), strdate.getMonth(), 0);
    // console.log(endofmonth);
    if (currentmonthlastday.getMonth() == 0 || currentmonthlastday.getMonth() == 1) {


    }
    if (strdateendofmonth.getFullYear() == currentmonthlastday.getFullYear() && strdateendofmonth.getMonth() - currentmonthlastday.getMonth() <= 1) {
      gracedatetd.item(i).style.backgroundColor = "yellow";
      gracedatetd.item(i).style.color = "black";
    } else if (strdateendofmonth.getFullYear() == currentmonthlastday.getFullYear() && strdateendofmonth.getMonth() - currentmonthlastday.getMonth() < 1) {
      gracedatetd.item(i).style.backgroundColor = "red";
      gracedatetd.item(i).style.color = "black";
    }
    // console.log(gracedatetd.item(i).innerHTML);
  }
}


function displaytime() {
  var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  var today = new Date();
  var d = today.getDate();
  var m = today.getMonth();
  var month = months[m];
  var y = today.getFullYear();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('clock').innerHTML =
  month + " " + d + ", " + y + " | " + h + ":" + m + ":" + s;
  var t = setTimeout(displaytime, 500);
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
$(document).ready(function(){
  if (sessionStorage.getItem('tracker') === null){
    console.log(sessionStorage);
    $('#flightfollower').val('Kyle Green');
    sessionStorage.setItem('tracker', $('#flightfollower').val());
  } else {
    $('#flightfollower').val(sessionStorage.getItem('tracker')).change();
  }
  $('#flightfollower').on('click', function() {
    sessionStorage.setItem('tracker', $('#flightfollower').val());
  });
});

function sleep(millis)
{
	var date = new Date();
	var curDate = null;
	do { curDate = new Date(); }
	while(curDate-date < millis);
};

function formatDate(date) {
  var monthNames = [
	"January", "February", "March",
	"April", "May", "June", "July",
	"August", "September", "October",
	"November", "December"
  ];

  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();
  return year + '-' + (monthIndex+1) + '-' + day + ' ' + date.getHours() + ':' + date.getMinutes()  + ':' + date.getSeconds() + ':' + date.getMilliseconds();
}
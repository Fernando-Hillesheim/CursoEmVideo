var date = new Date()
var hour = date.getHours()
var minutes = date.getMinutes()
if(minutes == 0){
    console.log(`Now it\' ${hour} o'clock!`);
} else{
    console.log(`Now it\'s ${hour} hours and ${minutes} minutes!`);
}
if(hour < 6) {
    console.log('It\'s the middle of the night');
} else if(hour < 12) {
    console.log('Good morning!');
} else if(hour < 18){
    console.log('Good afternoon!');
} else {
    console.log('Good evening!');
}
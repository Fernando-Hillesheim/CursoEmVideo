var data = new Date()
var day = data.getDay()
/*
0 - sunday
1 - monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - friday
6 - saturday
*/
var msg = 'Today is '

// day = 0

switch(day) {
    case 0:
        msg += 'Sunday'
        break
    case 1:
        msg += 'Monday'
        break
    case 2:
        msg += 'Tuesday'
        break
    case 3:
        msg += 'Wednesday'
        break
    case 4:
        msg += 'Thursday'
        break
    case 5:
        msg += 'Friday'
        break
    case 6:
        msg += 'Saturday'
        break
    default:
        console.log('Error! Invalid day!');
        break
}

console.log(msg);
# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#


function timeConversion(minutes){
  var x = minutes;
    if (x >= 60){
    hours = (x - x%60)/60; //*gives only the whole number - quotient*//

    return (hours + ":" + x%60);
  }
      else if (x < 60){
        hours = 0;

        return (hours + ":" + x);
  }
}

timeConversion(15);

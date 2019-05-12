/*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length
function makeLine(length) {
    var line = "";
    for (var j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

function buildTriangle(num){
    var triangle = "";
    for (var i = 1; i <= num; i += 1){
        triangle += makeLine(i);
    }
    return triangle;
}
console.log(buildTriangle(10));

// your code goes here.  Make sure you call makeLine() in your own code.


// test your code by uncommenting the following line
//console.log(buildTriangle(10));

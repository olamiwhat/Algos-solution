/* Code is a while loop that loops thru numbers 1 to 20
*checks if number is divisible by 3, 5 and 15 and prints string for each
*prints number if it's not divisible*/

var x = 1;

while (x <= 20 /* your stop condition goes here */) {
    // check divisibility
    // print Julia, James, or JuliaJames
    // increment x
}

var x = 1;

while (x <= 20) {
  if (x % 15 === 0){
    console.log("JuliaJames");
    }
    else if (x % 3 === 0){
        console.log("Julia");
    }
    else if (x % 5 === 0){
        console.log("James");
    }
 else {
     console.log(x);
 }
   x = x + 1;
}

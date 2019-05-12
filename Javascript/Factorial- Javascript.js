//* A code that runs the factorial of any number*//

function factorial(num){
    var solution = 1;
    for(var x = num; x > 1; x--){
      solution *= x;  //*This holds the new number as the code runs thru the for loop*//
    }
    return solution;
}
    factorial(25);

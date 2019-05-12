/*Write a for loop that prints out the factorial of the number 12:*/


var solution = 1;
for(var x = 12; x > 1; x -=1){
        solution *= x;
}
    console.log(solution);




    /*
     * Programming Quiz: Find my Seat (4-8)
     *
     * Write a nested for loop to print out all of the different seat combinations in the theater.
     * The first row-seat combination should be 0-0
     * The last row-seat combination will be 25-99
     *
     * Things to note:
     *  - the row and seat numbers start at 0, not 1
     *  - the highest seat number is 99, not 100
     */

    // Write your code here

    for (var seatRow = 0; seatRow < 26; seatRow += 1){
        for(var seatNum = 0; seatNum < 100; seatNum += 1){
            console.log(seatRow+ "-"+ seatNum);
        }
    }

function oddBall(numbers){
  var oddsum = ""
  for(i = 0; i < numbers.length; i ++){
    indsum = numbers[i]

    if (indsum % 2 !== 0){
      oddsum = oddsum + indsum
    }
    return oddsum;
  }
}

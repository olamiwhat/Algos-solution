# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.

function sumNum(num){
  var y = 0;
  for(var i = num; i >= 0; i--){
    y += i;
  }
  return y;
}

sumNum(5);

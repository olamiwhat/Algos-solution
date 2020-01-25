// Solution for Prime Number


function is_prime(num){
  if(num === 1){
    return false
  }
  const numFac = []
  for (let i = 1; i <= num; i++){
    if (num%i === 0){
      numFac.push(i)
      if (numFac.length > 2){
        return false
      }
    }
  }
  return true
}

console.log(is_prime(87456))

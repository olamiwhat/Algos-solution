function palindrome(string){
newString = ""
  for(i = 0; i < string.length - 1; i++){
    newString += string[i]
  }
  return newString
}


# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"


count = 0

while True:
  color = input("enter a rainbow color: ")
  rainbow = "red orange yellow green blue indigo violet"
  if color in rainbow:
    print (color, "is a rainbow color")
    break
    
  if color not in rainbow:
    print (color, "is not a rainbow color")
    count += 1
    if count == 4:
      print ("You have used all attempts!")
      break
  

print("End of Game!")

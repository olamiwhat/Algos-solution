#program taking 3 guess


#list bird names
bird_names = ("dove", "sparrow", "parrot")
#get input from user
bird_guess = input("Enter a bird name: ").lower()
#check input to True or False
res = bird_guess in bird_names

if res == True:
  print("Yes, 1st try")
else:
  if res == False:
    #get another input
    bird_guess = input("1st try wrong, enter a bird name: ").lower()
    res = bird_guess in bird_names
    if res == True:
      print("Yes, 2nd try")
    elif res == False:
      bird_guess = input("2nd try wrong, enter a bird name: ").lower()
      res = bird_guess in bird_names
      if res == True:
        print ("Yes, 3rd try!")
      else:
        print("sorry, you lost")
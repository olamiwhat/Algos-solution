#
#Program: str_analysis() Function
#Create the str_analysis() function that takes 1 string argument and returns a string message.
#The message will be an analysis of a test string that is passed as an argument to str_analysis().
#The program will call str_analysis() with a string argument from input collected within a while loop.
#The while loop will test if input is empty (an empty string "") and
#continue to loop and gather input until the user submits at least 1 character (input cannot be empty).
#The program then calls the str_analysis() function and prints the return message.



s = input("enter a word or integer: ")
while s == "":
  s = input("enter a word or integer: ")
if s != "":
  def str_analysis (s):
    if s.isdigit():
      if int(s) > 99:
        print ("Wow! I see you like 'em big")
      else:
        print("That is rather too small!")
    elif s.isalpha():
      print (s, "is an alphabetical string")
    else:
      print(s, "is neither digits nor alphabetical string")

str_analysis(s)
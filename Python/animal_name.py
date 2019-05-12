#Program: Animal Names
#Use while to get the user input, animal_name, of 4 animals
#use a counter, num_animals, in the while loop condition
#append the names to a string variable, all_animals
#User can exit early by typing "exit" (check if animal_name is "exit" and break)
#when the loop finishes, print the names of all_animals
#-bonus: print "no animals" if animal_name is empty after exiting the loop


num_animals = 0
all_animals = ""


while True:
  animal_name = input("enter the name of an animal, (type 'exit' to exit early): ")
  if animal_name != "exit":
    if num_animals == 3:
      animal_name = '\"' + animal_name + '\"'
      all_animals += animal_name
    else:
      animal_name = '\"' + animal_name + '\"'
      all_animals += animal_name + ", "
    num_animals += 1
  else:
    if animal_name == "exit":
      if len(all_animals) == 0:
        print("exiting.....\nno animal name entered!")
      break
         #print(all_animals)   
  if num_animals >= 4:
    break
print(all_animals)


#A program that takes a guess and checks
#if it is right or not
#it allows 3 attempts

def check_guess(letter, guess):
  if guess.isalpha() != True:
    print ("Guess is invalid")
    return False
  
  elif guess > letter:
    print ("Guess is high!")
    return False
  
  elif guess < letter:
    print("Guess is low!")
    return False

  else:
    print("Your guess is correct!")
    return True



#check_guess(letter, guess)


def letter_guess(letter = "j"):
  guess = input("Enter a letter: ").lower()
  guess_attempt = 1
  #check_guess(letter, guess)
  while check_guess(letter, guess) == False:
    guess = input("Please, try again!: ").lower()
    guess_attempt += 1
    if guess_attempt == 3:
      if check_guess(letter, guess) == True:
        break
      else:
        print("YOU LOST!!!")
        return False
  print ("Congratulations, You won the game!")
  return True
  

letter_guess()
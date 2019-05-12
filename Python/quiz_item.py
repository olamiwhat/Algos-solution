#create a function: quiz_item() that asks a question and tests if input is correct
#quiz_item()has 2 parameter strings: question and solution
#shows question, gets answer input
#returns True if answer == solution or continues to ask question until correct answer is provided



question = "Who is the 45th President of the United States?"
solution = "Donald Trump"

def quiz_item (question, solution):
  print (question)
  answer = input("answer: ")
  while answer.lower() != solution.lower():    
    print (question)
    answer = input("answer: ")
    if answer.lower() == solution.lower():
      break
  return True

print (quiz_item(question, solution))
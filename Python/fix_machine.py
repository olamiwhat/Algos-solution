#Just some codes ==> basic I would say

#Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

def fix_machine(debris, product):
  f_pos = 0
  new_string = ""
  while True:
    if debris.find(product[f_pos]) == -1:
      return "Give me something that's not useless next time."
    else:
      f_c = product[f_pos]
      new_string = new_string + f_c
      f_pos = f_pos + 1
      if new_string == product:
        return product
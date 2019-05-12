# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).


print ("Enter your name and date of birth (e.g 29,02,2000) to find out if you're a leap year baby!")
name = input("enter name: ").capitalize()

day = int(input("day: "))
if day not in range(1, 32):
  print(day, "is not a valid day of the month")
  input("enter day: ")
pass

month = int(input("month: "))
if month not in range(1, 13):
  print(month, "is not a valid month of the year")
  input("enter month: ")
pass

year = int(input("year: "))


def is_leap_baby(day,month,year):  
    if month == 2 and day == 29:
        if year % 100 == 0:
            if year % 400 == 0 and year % 4 == 0:
                return True
            return False
    #else if it is not divisible by 100 but divisible by 4, then it is a leap year
        elif year % 4 == 0:
            return True
        return False
    return False

# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.
status = is_leap_baby(day,month,year)

def output(status,name):
    if status:
        print ("%s is one of an extremely rare species. He is a leap year baby!" % name)
    else:
        print ("There's nothing special about %s's birthday. He is not a leap year baby!" % name)


output(status, name)
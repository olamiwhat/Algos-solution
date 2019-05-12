# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#



#To check if year is a leap year or not
def isLeapYear(year):
  #if a year is divisible by 100, it needs to also be divisible by 400 and 4 to be a leap year
  if year % 100 == 0:
    if year % 400 == 0 and year % 4 == 0:
      return True
    return False
  #else if it is not divisible by 100 but divisible by 4, then it is a leap year
  elif year % 4 == 0:
    return True
  return False


#calculating the days between dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  common_year = 365
  days_btw_years = 0
    #list of months with 30 days
  month_30days = (4,6,9,11)
  unlived_days1 = 0
  unlived_days2 = 0

  #to calculate the days between the 2 years
  for year in range(year1, year2+1):
    if isLeapYear(year):
      year = 366
    else:
      year = common_year
       
    days_btw_years += year

  #to calculate the number of unlived days in the birth year
  #starting from first month and counting to month before birth month
  for month in range(1, month1):
    if month == 2:
      if isLeapYear(year1):
        days = 29
      else:
        days = 28
    elif month in month_30days:
      days = 30
    else:
      days = 31
    #adding the days between the months
    unlived_days1 += days
  #including the days in the birth month
  unlived_days1 += day1-1
  #print (unlived_days1)
  

  #to calculate the number of unlived days in last year
  #starting from current month and counting down to the last month of the year
  for month in range(month2, 13):
    if month == 2:
      if isLeapYear(year1):
        days = 29
      else:
        days = 28
    elif month in month_30days:
      days = 30
    else:
      days = 31
    #adding days between the months
    unlived_days2 += days
  #print (unlived_days2)
  unlived_days2 -= day2-1
  unlived_days = unlived_days1 + unlived_days2
  
  #calculate days between dates
  days_btw_dates = days_btw_years - unlived_days

  return days_btw_dates

#print(daysBetweenDates(1985,6,16,2018,12,25))

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

#Program: quote_me() Function
#quote_me takes a string argument and returns a string that will display surrounded with added double quotes if printed



def quote_me(s):
 
  if s.startswith("\""):
    s = "\'" + s + "\'"
    print(s)
  else:
    s = '\"' + s + '\"'
    print(s)


quote_me("'Thank God'")
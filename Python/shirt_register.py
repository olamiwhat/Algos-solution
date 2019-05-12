#program for shirt register



shirt_small = 0
shirt_medium = 0
shirt_large = 0

while True:
  shirt_size = input("enter shirt size (S/M/L), or type \"exit\" (to finish): ")
  if shirt_size.lower().startswith("e"):
    confirm = input("are you sure? enter Y/N: ").lower()
    if confirm == "y":
      print ("Thank you, now exiting!")
      break
    else:
      pass
  elif shirt_size.lower() == "s":
    shirt_small += 1
    cost_s = shirt_small * 6
    
  elif shirt_size.lower() == "m":
    shirt_medium += 1
    cost_m = shirt_medium * 7
    
  elif shirt_size.lower() == "l":
    shirt_large += 1
    cost_l = shirt_large * 8
    
  else:
    print("Invalid selection, try again")

print("Small =",shirt_small, "Medium =",shirt_medium,"Large =", shirt_large)
print("subtotal cost; Small = $"+str(cost_s),"Medium = $"+str(cost_m),"Large = $"+str(cost_l))
print("Total cost = $"+str((cost_s + cost_m + cost_l)))
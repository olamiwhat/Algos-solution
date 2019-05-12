#ordering cheese


max_value = 100.0
min_value = 0.25
price = 2

order_amount = float(input("Enter cheese order weight (numeric): "))

def cheese_cost(order_amount):
  if (order_amount) > max_value:
    print (str(order_amount), "is more than the currently available stock")
  elif (order_amount) < min_value:
    print (str(order_amount), "is below minimum order amount")
  else:
    cost = price * order_amount
    print (order_amount, "costs $"+str(cost))


cheese_cost(order_amount)
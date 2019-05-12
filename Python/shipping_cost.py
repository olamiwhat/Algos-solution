#This program calculates the cheapest Shipping Method
#and Cost to ship a package at Sal's shipping
weight = int(input("Please, enter the weight of your package: "))
#define premium shipping cost as a variable
premium_shipping = 125.00

#Function to calculate cost of ground shipping
def ground_shipping (weight):
  flat_rate = 20
  if weight <= 2.0:
    cost = (1.5 * weight) + flat_rate
    return cost
  elif weight <= 6.0:
    cost = (3 * weight) + flat_rate
    return cost
  elif weight <= 10.0:
    cost = (4 *weight) + flat_rate
    return cost
  else:
    cost = (4.75 * weight) + flat_rate
    return cost
    
#Test Function (uncomment)
#print(ground_shipping (8.4))

#Function to calculate cost of drone shipping
def drone_shipping (weight):
  if weight <= 2.0:
    cost = (4.5 * weight)
    return cost
  elif weight <= 6.0:
    cost = (9 * weight)
    return cost
  elif weight <= 10.0:
    cost = (12 *weight)
    return cost
  else:
    cost = (14.25 * weight)
    return cost
  
#Test Function(uncomment)
#print(drone_shipping (1.5))

#Function to determine the cheapest shipping method and cost
def cheapest_shipping_method_and_cost(weight):
  
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_shipping
  
  if ground < drone and ground < premium:
    print("Your cheapest shipping method is ground shipping, it will cost " + "$" + str(ground))
  elif ground > drone and drone < premium:
    print("Your cheapest shipping method is drone shipping, it will cost " + "$" + str(drone))
  else:
    print("Your cheapest shipping method is premium shipping, it will cost " + "$" + str(premium))
    
#Calculating the cheapest way to ship 4.8lb and 41.5lb of packages
cheapest_shipping_method_and_cost(weight)
#cheapest_shipping_method_and_cost()

def ground_shipping(weight):
      if (weight <= 2):
    cost = weight * 1.50 + 20.00
    return cost
  elif (weight > 2 and weight <= 6):
    cost = weight * 3.00 + 20.00
    return cost
  elif (weight > 6 and weight <= 10):
    cost = weight * 4.00 + 20.00
    return cost
  else:
    cost = weight * 4.75 + 20.00
    return cost
#END of ground_shipp function

#PRIME SHIPPING
premium_shipping = 125.00

def drone_shipping(weight):
  if (weight <= 2):
    cost = weight * 4.50
    return cost
  elif (weight > 2 and weight <= 6):
    cost = weight * 9.00
    return cost
  elif (weight > 6 and weight <= 10):
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost
#END OF drone_shipping function

def cheapest_method(weight):
  total_ground = ground_shipping(weight)
  total_drone = drone_shipping(weight)
  
  if (total_ground < total_drone and total_ground < premium_shipping):
    return "The total is " + str(total_ground) + " , and you need to use this method since ground shipping is cheaper." 
  elif (premium_shipping < total_drone):
    return "The total is " + str(premium_shipping) + " , and you need to use this method since premium shipping is cheaper." 
  else:
    return "The total is " + str(total_drone) + " , and you need to use this method since drone shipping is cheaper."
  

#CALCULATION ARE CORRECT!!!  
print(cheapest_method(41.5))
def mpg (miles, gallons):
  mpg = float (miles) / float (gallons)

  return mpg


def cost (mpg):
  price = 2.50
  cost = float (mpg)*price

  return cost

name = input("Enter destination city ")
miles = float (input("Enter miles travelled "))
gallons = float (input("Enter total gallons used "))

mpg = mpg (miles, gallons)
cost = cost (mpg)

print("Driving to  ", name)
print("will be ", miles, " miles")
print("and will cost ", cost, "$")

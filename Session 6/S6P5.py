def rate (hours, code):
  if code == "I":
    rate = 250
  elif code == "O":
    rate = 550
  else:
   rate = 10

  cost = hours * rate

  return cost


name = input("Enter your last name ")
code = str (input("Please enter district code "))
hours = float (input("Please enter credit hours wanted "))

cost = rate (hours, code)

print( name)
print("total ", cost, " $")

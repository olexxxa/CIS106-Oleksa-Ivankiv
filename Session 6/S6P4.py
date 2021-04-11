def rate (code):
  if code == "L":
    rate = 25
  elif code == "A":
    rate = 30
  elif code == "J":
    rate = 50
  else:
   rate = 10

  return rate


def gross (hours, rate):
  if hours > 40:
    hours = ((hours - 40) * 1.5) + 40
  else:
    hours = hours


  gross = hours * rate

  return gross

name = input("Enter your last name ")
code = str (input("Please enter job code "))
hours = float (input("Please enter hours worked "))

rate = rate (code)
gross = gross (hours, rate)

print( name)
print("Gross ", gross, " $")

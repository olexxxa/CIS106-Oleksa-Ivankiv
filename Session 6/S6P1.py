def totalc(qty,price):
  total = float(qty) * float(price)
  
  if total > 10000.00:
    total = total * 0.90
  else:
    total = total
  
  return total

qty = float(input("Enter quatity"))
price = float(input("Enter the price"))

total = totalc(qty,price)

print ("Total is", total)

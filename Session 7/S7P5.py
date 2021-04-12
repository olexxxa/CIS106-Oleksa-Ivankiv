x = 0.07 #variable x with global scope

def comptotal(qty, price):
  total = float(qty) * float(price)
  tax = total*x
  return total, tax



qty = float(input("Enter quantity"))
price = float(input("Enter price"))

total, tax = comptotal(qty,price)

print("total is $", total)
print("tax is $", tax)

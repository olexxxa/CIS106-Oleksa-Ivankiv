partn = int(input("Enter the part number you want to purchuase "))
qty = (input("Enter quantity of items you want to purcuase "))

if partn == 10 or partn == 55:
    unitprice = 1.00
elif partn == 99:
    unitprice = 2.00
elif partn == 80 or partn == 70:
    unitprice = 3.00
else:
    unitprice = 5.00

total = float(qty) * unitprice

print("Part number:  ", partn)
print("Quantity:     ", qty)
print("Unit price:   ", unitprice)
print("Total:        ", total)

f=open("data2.txt")
average = 0
c = 0
totalprice = 0
eprice = 0
lastname = f.readline()

while lastname != "":
  quantity = f.readline()
  price = f.readline()
  eprice = float(quantity) * float(price)
  print()
  print("Item Name, quantity and price: ", lastname, quantity, price)
  print("Extended price: $", eprice)
  totalprice = float(totalprice) + float(eprice)
  c = c + 1
  lastname = f.readline()
print(" ")
average = totalprice/c
print("Average: $", average )

f.close()


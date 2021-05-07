f=open("data3.txt")
tutionowned = 0
c = 0
totalprice = 0
price = 250
lastname = f.readline()

while lastname != "":
  credits = f.readline()
  eprice = float(credits) * float(price)
  print()
  print("Student Last Name, credits taken and price per credit: ", lastname, credits, price)
  print("Tution owed: $", eprice)
  totalprice = float(totalprice) + float(eprice)
  c = c + 1
  lastname = f.readline()
print(" ")
print("Total tution owed for all studens and students number: $", totalprice, ":" , c )

f.close()


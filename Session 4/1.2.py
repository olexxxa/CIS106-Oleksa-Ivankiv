print("Please input Item name 'A' or 'B'")
uN = input()
print("Please input quantity")
q = int(input())
if uN == "A":
    uP = 10
    tP = q * uP
else:
    uP = 20
    tP = q * uP
print("Item entered is " + uN + ", Unit price is " + str(uP) + ", Extended price is " + str(tP))

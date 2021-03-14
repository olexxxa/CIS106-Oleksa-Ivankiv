print("Please enter appliance name")
uN = input()
print("Please input price")
uP = int(input())
if uP > 1000:
    wP = uP * 0.1
    tP = uP + wP
else:
    wP = uP * 0.05
    tP = uP + wP
print("Item name entered is " + uN + ", Unit price is " + str(uP) + ", Warantee price is " + str(wP) + ", Grand total ammount is " + str(tP))

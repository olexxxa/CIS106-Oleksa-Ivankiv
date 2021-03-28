print("Please enter quantity of tickets you want to purchuase")
q = float(input())
if q >= 25:
    tP = 50
else:
    if q >= 10:
        tP = 60
    else:
        if q >= 5:
            tP = 70
        else:
            tP = 75
total = q * tP
print("Nubmer of tickets: " + str(q) + ", price per ticket is " + str(tP) + ", total cost is " + str(total))

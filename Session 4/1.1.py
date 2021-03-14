t = 0.07
print("Please input Quatity of items")
q = int(input())
if q < 1000:
    p = 5.0
    eP = q * p
    fP = eP * t + eP
else:
    p = 3.0
    eP = q * p
    fP = eP * t + eP
print("Quantity is " + str(q) + ", Unit price is " + str(p) + ", Extended price is " + str(eP) + ", Tax is " + str(t * 100) + "%," + " Total amount is " + str(fP))

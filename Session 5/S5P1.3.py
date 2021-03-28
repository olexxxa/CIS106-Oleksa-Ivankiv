print("Please enter principle amount")
pA = int(input())
print("Please enter years to maturity")
y = float(input())
if pA > 100000 and y == 5:
    iR = 0.06
else:
    if pA > 50000 and y == 10:
        iR = 0.05
    else:
        if pA > 50000 or y == 5:
            iR = 0.04
        else:
            iR = 0.02
total = pA * iR
print("Principle is " + str(pA) + ", Interest rate is " + str(iR) + ", Total interest amount for the first year is " + str(total))

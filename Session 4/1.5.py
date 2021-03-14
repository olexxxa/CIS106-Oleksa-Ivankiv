print("Please enter your last name")
uN = input()
print("Please input number of dependents")
dQ = int(input())
print("Please enter your gross income")
gI = int(input())
aGI = gI - dQ * 12000
if aGI > 50000:
    tR = 0.2
    iT = aGI * tR
else:
    if aGI >= 0:
        tR = 0.1
        iT = aGI * tR
    else:
        iT = 100
print("Your last name entered is " + uN + ", Gross income is " + str(gI) + ", Number of dependence is " + str(dQ) + ", Adjusted gross income is " + str(aGI) + ", Income tax is " + str(iT))

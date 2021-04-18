print("Do you want to compute income tax?")
yes = input()
while yes == "Yes":
    print("Plase enter Your gross income")
    gI = float(input())
    if gI > 500000:
        t = 0.3
    else:
        if gI > 200000:
            t = 0.2
        else:
            t = 0.15
    tO = gI * t
    print("Gross income is" + str(gI) + " Tax rate is " + str(t) + " Tax owed is " + str(tO))
    print("Do you want to repeat the program? (Yes or No)")
    yes = input()

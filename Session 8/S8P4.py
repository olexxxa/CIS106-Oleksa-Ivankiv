print("Do you want to start the program?")
yes = input()
while yes == "Yes":
    print("Plase enter item name than enter, item price then enter and quantity and enter")
    iN = input()
    iP = float(input())
    q = float(input())
    eP = iP * q
    if eP > 10000:
        d = 0.1
    else:
        if eP > 5000:
            d = 0.05
        else:
            d = 0.02
    dA = eP * d
    dP = eP - dA
    t = dP * 0.07
    print("Item" + iN + " Extended price is " + str(eP) + " Discount amount is " + str(dA) + " Discounted price is " + str(dP) + " Tax is " + str(t))
    print("Do you want to repeat the program? (Yes or No)")
    yes = input()

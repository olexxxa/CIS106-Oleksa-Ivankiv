print("Enter number of books to order")
q = int(input())
print("Please enter price per book")
p = int(input())
tP = q * p
if tP > 50:
    sP = 0
else:
    sP = 25
    tP = tP + sP
print("Order total is " + str(tP) + "$" + ", including shipping cost - " + str(sP) + "$")

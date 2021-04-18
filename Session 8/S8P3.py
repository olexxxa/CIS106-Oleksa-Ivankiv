print("Do you want to start the program?")
yes = input()
while yes == "Yes":
    print("Plase enter last name than enter, first exam score then enter and second exam score")
    fN = input()
    s1 = int(input())
    s2 = int(input())
    aV = float((s1 + s2)) / 2
    print("Average is" + str(aV))
    print("Do you want to repeat the program? (Yes or No)")
    yes = input()

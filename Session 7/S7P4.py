def comp (sc1,sc2,sc3,hc):
  av = (sc1+sc2+sc3)/3
  avh = (sc1+sc2+sc3+3*hc)/3
  return av,avh

name = (input("Enter player name "))
sc1 = float (input("Please enter 1st score "))
sc2 = float (input("Please enter 2nd score "))
sc3 = float (input("Please enter 3rd score "))
hc = float (input("Please enter handicap "))


av, avh = comp(sc1,sc2,sc3,hc)


print("Player ", name)
print("Average score is ", av)
print("Average score with handicap is ", avh)

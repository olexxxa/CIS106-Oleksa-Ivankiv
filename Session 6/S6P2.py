def battlingav (totalhits, totalatbats):
  average = float (totalhits) / float (totalatbats)

  return average

name = input("Enter player's last name ")
totalhits = float (input("Enter total number of hits "))
totalatbats = float (input("Enter total number of atbats "))

average = battlingav(totalhits, totalatbats)

print(name, "battling average is ")
print(average)

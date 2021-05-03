def ai (interest, amount):
  a1 = interest*amount+amount
  return a1

def ai2 (interest, a1):
  a2 = interest*a1+a1
  return a2

def ai3 (interest, a2):
  a3 = interest*a2+a2
  return a3

def ai4 (interest, a3):
  a4 = interest*a3+a3
  return a4

def ai5 (interest, a4):
  a5 = interest*a4+a4
  return a5



print("Do you want to compute the annual interest?")
yes = input()
while yes == "Yes":
  print("Please enter Your principle amount")
  amount = float(input())
  print("Please enter Your interest rate")
  interest = float(input()) 
  
  a1 = ai(interest,amount)
  a2 = ai2(interest,a1)
  a3 = ai3(interest,a2)
  a4 = ai4(interest,a3)
  a5 = ai5(interest,a4)

  total = a5 - amount
  print ("1 Year beginning balance is",amount," Ending balance is ",
  a1)
  print ("2 Year beginning balance is",a1," Ending balance is ",
  a2)
  print ("3 Year beginning balance is",a2," Ending balance is ",
  a3)
  print ("4 Year beginning balance is",a3," Ending balance is ",
  a4)
  print ("5 Year beginning balance is",a4," Ending balance is ",
  a5)
  print ("Total earning is ",total)
  
  print("Do you want to repeat the program? (Yes or No)")
  yes = input()

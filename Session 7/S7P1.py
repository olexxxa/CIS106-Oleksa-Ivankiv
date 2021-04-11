def comdisc (qty, price, rate):
  total = float(price)*float(qty)

  disctotal = total - (total * rate/100)

  discprice = price - (price * rate/100)

  return disctotal, discprice

qty = float (input("Enter quantity "))
price = float (input("Please enter price per quatity "))
rate = float (input("Please enter discount rate "))

disctotal, discprice = comdisc(qty,price,rate)


print("Qantity is ", qty)
print("Price is ", price, " $")
print("Discounted price is ", discprice, " $")
print("Discounted total is ", disctotal, " $")

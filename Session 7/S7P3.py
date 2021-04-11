def comp (sales):
  if sales > 100000:
    commission = 0.10
  else:
    commission = 0.05

  target = sales * 0.05

  return target, commission

name = (input("Enter salesperson name "))
sales = float (input("Please enter sales amount "))


target, commission = comp(sales)


print("Salesperson ", name)
print("Commission is ", commission)
print("Next year target is ", target)

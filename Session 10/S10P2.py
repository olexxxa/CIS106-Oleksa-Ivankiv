def printarray(arr, scarr):
  print ("List of names with scores:")
  print(arr[0],scarr[0])
  print(arr[1],scarr[1])
  print(arr[2],scarr[2])
  print(arr[3],scarr[3])


def printreverse(arr, scarr):
  arr.reverse()
  scarr.reverse()
  print ("Reversed list of names with scores:")
  print(arr[0],scarr[0])
  print(arr[1],scarr[1])
  print(arr[2],scarr[2])
  print(arr[3],scarr[3])


arr = ['Ivankiv','Todorov','Hrab','Kotil']
scarr = [98,90,99,80]
printarray(arr, scarr)
print()
printreverse(arr, scarr)

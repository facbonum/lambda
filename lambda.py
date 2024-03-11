#def squared(num): return num * num
squared = lambda num : num * num

print(squared(2))


addTwo = lambda num : num + 2




print(addTwo(12))


############################
def funcBuilder(x):
  return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))
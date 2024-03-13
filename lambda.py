# We can assign a lambda to a variable,
# but because they are anonymous functions, they can not be called directly
# VS Code may reformat lambdas automatically
# def squared(num): return num * num

squared = lambda num : num * num
print(squared(2))

# def addTwo(num): return num + 2
addTwo = lambda num : num + 2
print(addTwo(12))


############################
def funcBuilder(x):
  return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

# def sum(a, b): return a + b
# sum = lambda a, b : a + b
# print(sum(2,3))
# print(sum(10,8))

###########################
numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))
# returns result applied to each item in a data collection

odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))
# filters out anything that does not return True in this function
###########################

from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr,
numbers, 10)

print(total)

print(sum(numbers, 10))

lambda acc, curr : acc + len(curr)

names = ['Dave', 'Sara', 'John']
char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)
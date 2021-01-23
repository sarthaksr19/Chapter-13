divisible5 = lambda num: num%5 == 0

l = [25,65,10,5,7,8,50,60]
print(list(filter(divisible5,l)))
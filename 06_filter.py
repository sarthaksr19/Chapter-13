def gt5(num):  #finding the number which is greater than 5 in all the list values.
    if num > 5:
        return True
    else:
        return False

gt10 = lambda num: num>10  #using lambda function we find greatest number 10


l = [1,56,8,7,6,952,4,14,2,56,89,23]
print(list(filter(gt5,l)))  
print(list(filter(gt10,l)))
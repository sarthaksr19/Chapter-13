def square(num):
    return num * num

l = [3,5,7,9]

# Method 1 for getting the square of all the values of list
l2 = []
for i in l:
    l2.append(square(i))
print(l2)

# method 2 with using map keyword

print(list(map(square,l)))  #map applies a function to all the items in the list.
# here square function is applied in the all item of the list l  
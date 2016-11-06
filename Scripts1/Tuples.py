#tuples

test1 = (10,11)
print(type(test1))
      
test2 = 10,11
print(type(test2))
      
test3 = (10,)
print(type(test3))

test4 = 10,
print(type(test4))

test5 = (10)
print(type(test5))

test6 = 10
print(type(test6))


#list to tuple

list1 = [5, 2, 1]
print(list1)
tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))

#accessing members of tuple

tuple1 = (1, 2, 3)
print(tuple1[1])

#slicing
tuple2 = (2, 4, 5, 6, 9, 0)
sliced = tuple2[2:5]
sliced2 = tuple2[2:3]
print(sliced)
print(sliced2)


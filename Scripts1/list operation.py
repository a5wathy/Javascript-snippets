#list operatios

#addition and multiplication
test1 = [5,3,1]
test2 = [1,4,2]
add = test1 + test2
add2 = test2 + test1

print(add)
print(add2)


mul = test1*2

print(mul)

#string to list

test3= "Aswathy.Gopalakrishnan"

test_list = list(test3)

print(test_list)

# in and not in operation
print("A in list test3", "A" in test3)
print("A in list test3", "A" not in test3)

#assigning part of a list to another list
test = [54, 4, 879, 62]

#min,max and len functions

print(min(test))
print(max(test))
print(len(test))
      
new_test =test[1:]

print(new_test)

#assigning to slice of a list

test2 = ["new","new","new","new"]

#test[2:] = test2
test[1:3] = test2
print(test)

#deleting an element of list

del test[2]
print(test)

#modify an element in list
test[3] = "old"
print(test)

#append
test.append("end")
print(test)

#count
print(test.count("new"))

#extend
test.extend([1000,1000])
print(test)

#index
print(test.index(54)) # if there are 2 similar ones, result gives the first one

#reverse
test.reverse()
print(test)

#sort
#test.sort()
#print(test) #error:unorderable list types
test1 = [2,4,3,5,1,9,0]
test1.sort()
print(test1)

#clear
test1.clear()
print(test1)


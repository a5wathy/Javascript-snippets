list1 = [1, 2, 3, 4, 5]

def square(x):
    return(x*x)

def cube(x):
    return(x*x*x)

def my_map(func, list1):
    result = []
    for num in list1:
        result.append(func(num))
    return result
    
squares = my_map(square, list1)
cubes = my_map(cube, list1)

print(squares, cubes)

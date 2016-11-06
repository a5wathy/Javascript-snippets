#contine,pass and break statements

number = 11

"""while number>=1:
    number-=1
    print(number)"""

#continue-skip printing number 5

"""while number>=1:
    number-=1
    if number == 5:
        continue
    print(number)"""

#break-break from loop at 5   
"""while number>=1:
    number-=1
    if number == 5:
        break
    print(number)"""

#pass=filler statement
"""while number>=1:
    number-=1
    if number == 5:
        pass
    print(number)"""

"""for number in range(10,-1,-1):
    print(number)"""
    
#break
"""for number in range(10,-1,-1):
    if number == 5:
        break
    print(number)"""

#continue
"""for number in range(10,-1,-1):
    if number == 5:
        continue
    print(number)"""
#pass
for number in range(10,-1,-1):
    if number == 5:
        pass
    print(number)

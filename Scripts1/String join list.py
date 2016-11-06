#string_value.join(list_name)

list_1 = ["I", "am" , "learning", "python"]

outputStr ="_".join(list_1)

print(outputStr)


#string functions

var ="Learn python"

print(var.title()) #converts first letter of each word into upper case and others to lower case


print(var.swapcase()) #upper case to lower case and vice versa

print(var.upper()) # all to upper case

print(var.lower()) #all to lower case

print(var.capitalize()) #only first letter becomes upper case.rest to lower case

#use of \

path = "C:\myfile"
print(path)
path = "C:\newfile"
print(path)
path = "C:\\newfile"
print(path)
path = r"C:\newfile"
print(path)

#infinite loop

while(True):
    pw = input("Enter the password:")
    if pw == "mypassword":
        break
    print("Try again")

print("Access Granted")

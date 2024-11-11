print("Maximum of three integers")
integer1 = int(input("1st integer= "))
integer2 = int(input("2nd integer= "))
integer3 = int(input("3rd integer= "))
if integer1 >= integer2 and integer1 >= integer3:
    maximum = integer1
elif integer2 >= integer1 and integer2 >= integer3:
    maximum = integer2
else:
    maximum = integer3
print("The maximum is:", maximum)
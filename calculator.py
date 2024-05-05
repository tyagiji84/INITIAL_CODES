x = int(input("enter the first number"))
y = int(input("enter the secont number"))
choice = str(input("enter your choice"))
if choice == "-":
    print(x-y)
elif choice == "+":
    print(x+y)
elif choice =="*":
    print(x*y)
else:
    print(x/y)
    
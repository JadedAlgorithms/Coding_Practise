def oddEven(a):
    if a%2==0:
        return 1
    else:
        return 0
a=int(input("Enter the number: "))
if oddEven(a)==1:
    print("Even")
else:
    print("Odd")
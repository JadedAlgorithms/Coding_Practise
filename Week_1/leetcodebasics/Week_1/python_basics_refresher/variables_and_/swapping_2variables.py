def swapVariables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
print("Enter the values:")
a=int(input("Enter: "))
b=(int(input("Enter: ")))
print(f"Orignal values of a: {a} and b: {b}")
a,b=swapVariables(a,b)  #I know python supports tupple unpacking!
print(f"New values of a: {a} & b: {b}")
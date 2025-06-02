def factorial(n):
    if n<=1:
        return n
    else: 
        return n*factorial(n-1)
n=int(input("Enter the number! "))
print(f"The factorial of {n} is {factorial(n)}")
def fibonacii(n):
    if n<=1:
        return n
    else: 
        return fibonacii(n-1)+fibonacii(n-2)
n=int(input("Enter the number of terms you want to display: "))
for i in range(0,n):
    print(fibonacii(i),end=" ")

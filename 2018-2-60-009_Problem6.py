def Fibo(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return Fibo(n-1)+ Fibo(n-2)

n = int(input("Enter number: "))
print(f"{n}-th Fibonacci number is: {Fibo(n)}")

    


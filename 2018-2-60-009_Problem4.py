N = int(input("Enter number: "))
sum= 0

for i in range (1 , N+1):
    if(i < 10):
        print(i ** 2, end= " + ")
    else:
        print(i ** 2, end= "  ")
    
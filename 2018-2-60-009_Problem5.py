
def prime_find_2018_2_60_009(N):
    c= 0
    for i in range (2, N):
        if N%i == 0:
            c+= 1
            break;
    if c == 0:
        print(f"{N} is Prime number")
    else:
        print(f"{N} is not Prime number")

N = int(input("Enter number: "))
prime_find_2018_2_60_009(N)
    
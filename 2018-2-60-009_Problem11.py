string= input("Enter String: ")

for i in range (0, len(string)):
    if (i%2==0):
        print(f"{string[i]}",end=" ")

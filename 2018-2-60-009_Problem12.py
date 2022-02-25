string=input("Enter string: ")
n=int(input("Enter number: "))
new_string=""
for i in range (0, len(string)):
    if i>n:
        new_string+=string[i]
print(f"{new_string}")

        
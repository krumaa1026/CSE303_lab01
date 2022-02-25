arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0
for i in range (0, len(arr)):
    if i%2 == 0:
        sum+= arr[i]
print(f"Sum is: {sum}")

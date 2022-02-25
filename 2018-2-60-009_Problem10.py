def second_largest_number_2018_2_60_009(arr):
    lv=arr[0]
    for i in range (0, len(arr)):
        if lv<arr[i]:
            lv=arr[i]
    slv=arr[0]
    for i in range (0, len(arr)):
        if slv<arr[i] and arr[i]!= lv:
            slv=arr[i]
    return slv

    
arr = [12, 24, 35, 4, 8, 6, 90, 55]
print(f"2nd Largest number is: {second_largest_number_2018_2_60_009(arr)}")

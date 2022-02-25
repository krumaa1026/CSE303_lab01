def  largest_number_2018_2_60_009(arr):
    lv=arr[0]
    for i in range (0, len(arr)):
        if lv<arr[i]:
            lv=arr[i]
    return lv
def smallest_number_2018_2_60_009(arr):
    sv=arr[0]
    for i in range (0, len(arr)):
        if sv>arr[i]:
            sv=arr[i]
    return sv
    
arr = [12, 24, 35, 4, 8, 6, 90, 55]
print(f"Largest number is: {largest_number_2018_2_60_009(arr)}")
print(f"Smallest number is: {smallest_number_2018_2_60_009(arr)}")

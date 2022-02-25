arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[5,10,15,20,25,30,35,40,45,50]
new_list=[]

for i in range (0, len(arr1)):
    if arr1[i]%2 != 0:
        new_list.append(arr1[i]) 

for i in range (0, len(arr2)):
    if arr2[i]%2 == 0:
        new_list.append(arr2[i]) 
print(new_list)


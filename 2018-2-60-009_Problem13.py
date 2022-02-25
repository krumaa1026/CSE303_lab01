string=input("Enter string: ")
sub_string="CSE303"
cnt=0
for i in range(0,len(string)):
    if string[i : len(sub_string)+i]==sub_string:
        cnt+=1
print(f"Count of substring: {cnt}")

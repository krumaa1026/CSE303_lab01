def palindrome_checker_2018_2_60_009(string):
    for i in range (0, len(string)):
        if string[ : : -1] ==string:
            return True
        else:
            return False
    
string =input("Enter string: ")
if(palindrome_checker_2018_2_60_009(string) == True):
    print("Is palindrome")
else:
    print("Is not palindrome")

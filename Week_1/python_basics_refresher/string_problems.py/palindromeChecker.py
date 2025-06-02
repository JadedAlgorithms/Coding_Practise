def isPalindrome(str):
    if str[::-1]==str:
        return True
    else: 
        return False
str=input("Enter the string ")
if isPalindrome(str)==True:
    print("it's a Palindrome! ")
else: 
    print("It's not a Palindrome!")
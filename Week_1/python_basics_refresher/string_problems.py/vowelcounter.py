def countVowels(string_id):
    string2=string_id.lower()
    vowels=0
    for i in string2:
        if i in ["a","e","i","o","u"]:
            vowels+=1
    return vowels
ch=input("Enter the string: ")
print(f"Number of vowels in the given string is {countVowels(ch)}")

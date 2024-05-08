#write a function that accepts a string and calculates the number of uppercase letters and lower case letters
upper=0
lower=0
def check_letter(s):
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    return upper,lower

m=input("Enter a sentence below and get the number of upper case letters and lower case letters: \n")
check_letter(m)
print(f"The number of upper case letters are : {upper}")
print(f"The number of lower case letters are : {lower}")
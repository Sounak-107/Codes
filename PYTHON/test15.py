# a function that could check if a string is palindrome or not
def palindrome(s):
    s= s.replace(' ','')
    m=''
    m= s[::-1]
    if m==s:
        print("the string is a palindrome")
    else:
        print("the string is not a palindrome")
        
a=input("Enter below the word you want to check: \n")
palindrome(a)
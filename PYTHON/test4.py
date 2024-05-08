# accept two word string and if both words begin with same letter return true else false
def check(m,s):
    m=m[0].lower()
    s=s[0].lower()
    if  (m==s) : 
        return True
    else:
        return False
    
a=input("Enter the word of your choice: ")
b=input("Enter the second word of your choice: ")   
check(a,b)   
# accept two word string and if both words begin with same letter return true else false
def check(m,s):
    m=m[0].lower()
    s=s[0].lower()
    if  (m==s) : 
        return True
    else:
        return False
    
    
print(check('hello','hi'))   
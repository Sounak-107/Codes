# function given a and b , if a +b = 20 return true if a or b = 20 or a+b != 20 return false
def myfunc(a,b):
    if a==20 or b==20 or a+b != 20:
        return False
    elif a+b==20 :
        return True
    
s=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))

myfunc(s,m)
    
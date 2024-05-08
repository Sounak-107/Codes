# a function that checks whether a number is in a given range (including high and low)
def check(c,s,m):
    if s<m:
        if s<=c<=m:
          return True
        else:
          return False
    elif m<s:
        if m<=c<=s:
            return True
        else:
            return False
    else: 
        return False


    
# main program 
a=int(input("Enter a number: "))
print("Now you have to input other numbers to check if the previous number is in range ")
b=int(input("Enter the 1st number: "))
d=int(input("Enter the 2nd number: "))

if check(a,b,d)==True:
    print(f"{a} is in the range ")
else:
    print(f"{a} is not in the range ")   
    
    
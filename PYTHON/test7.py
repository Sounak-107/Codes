#check if a number is within 10 of either 100 or 200, if yes return true if not return false
def check(n):
    if n in range(90,111,1) or n in range(190,211,1):
        return True
    else:
        return False 
    
print(check(250))
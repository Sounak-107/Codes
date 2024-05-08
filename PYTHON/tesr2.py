#understanding level 1
# function returns the lesser when both numbers are even and returns the greter when both or one of them is odd
def myfunc(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    elif a%2 != 0 or b%2 != 0:
        if a>b:
            return a
        else:
            return b


print(myfunc(9,2))
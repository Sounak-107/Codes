# a function that capitalizes 1st nd 4th letter of a name 
def myfunc(s):
    m=''
    count=0
    for x in range(len(s)):
        if count == 0:
            m=m+s[count].upper()
        elif count == 3 :
            m=m+s[count].upper()
        else:
            m=m+s[count]
        count +=1
    return m 

a=input("Enter a name or any word of your choice: ")
print(myfunc(a))
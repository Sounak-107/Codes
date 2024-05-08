# a function that multiply all the numbers in a list
def mul_num(s):

    mul=1
    for i in s:
        mul=mul*int(i)
    return mul

m=[]
i=1
a=int(input("How many numbers you want to add to the list?\n"))

while i<=a:
    b=int(input("Enter the numbers: "))
    m.append(b)
    i+=1

c= mul_num(m)
print(f"The multiple of every number of the stringn is : {c}")
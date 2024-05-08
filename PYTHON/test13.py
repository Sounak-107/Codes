#a function that takes a list and returns a new list with unique elements of the first list
def uni_list(m):
    m.sort()
    return set(m)

s=input("Enter a list: ")
a=uni_list(s)
print(a)
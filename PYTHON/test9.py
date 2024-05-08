#given a string return another where for every character in the original there are 3 characters
def times3(s):
    m=''
    for i in s:
       m = m+i*3
    return m

print(times3("hola"))
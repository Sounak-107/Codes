def myfunc(*args):
    mylist=[]
    for items in args:
        if items %2 == 0:
            mylist.append(items)
    return mylist
        
print(myfunc(1,2,3,4,5,6,7))
        

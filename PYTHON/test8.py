#understanding level 2
#given a list of ints return true if the array contains a 3 next to a 3 somewhere
def check_3(lst):
    for i in range(len(lst)-1):
        if lst[i]==3 and lst[i+1]==3:
            return True
        else:
            return False
        
print(check_3([1,3,3]))

#?/\
            
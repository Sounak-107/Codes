#check if a string is pangram or not
# pangram string: the string contains every letter of the alphabet at least once .
def pangram(s):
    s= s.replace(' ','')
    s=s.lower()
    for i in range(97,123):
        if chr(i) not in s:
            return False
    return True

a=input("Enter the sentence you want to check below: \n")
if pangram(a)== True:
    print("This sentece is a pangram")
else:
    print("This sentence is not pangram")
# returns 'FIZZ-BUZZ' when the number is divisable by 3 and 5, returns 'FIZZ' when the number is divisable only by 3, returns 'BUZZ' when the number is divisable only by 5, else returns the number itself
def divisability(low,up):
    for num in range(low,up+1,1):
        if num % 3 ==0 and num % 5 == 0:
            print('FIZZ-BUZZ')
        elif num % 3 == 0:
            print('FIZZ')
        elif num % 5 == 0:
            print('BUZZ')
        else:
            print(num)
            
s=int(input("Enter the lower range: "))
m=int(input("Enter the upper range: "))

divisability(s,m)
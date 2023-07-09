again='t'
while again=='t':
    c=int(input(' enter number is less than 25 : '))
    if c<25:
        if c%2==0:
            print(c,' is an even number ')
        else:
            print(c ,'is an odd number')
    else:
        print(c,' is greater than 25')
    again=input('if you want to try again write t : ')

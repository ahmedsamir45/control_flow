again='t'
while again=='t':
    x=float(input('enter the first number : '))
    y=float(input('enter the second number :'))
    if x>y:
        print(x,'>',y)
    elif x==y:
        print(x,"=",y)
    else:
        print(x,"<",y)
    again=input('if you want to calculate again enter t : ') 

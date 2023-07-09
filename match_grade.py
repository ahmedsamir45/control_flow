x = eval(input('enter your degree :'))
match x :
  case a if 60>x and x>=0:
   print('your grade F')
  case a if 60<=x and x<70:
    print('your grade D')
  case a if 71<=x and x<=75 :
    print('your grade C')
  case a if x>76 and x<=85  :
    print('your grade B')
  case a if x>85 and x<=100 :
    print('your grade A')
  case defult:
    print('error')

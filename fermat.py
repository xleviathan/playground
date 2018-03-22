def check_fermat(a,b,c,n):
    if n>2 and (a**n + b**n == c**n):
       print('Holy shit fermat was wrong')
    else:
        print("No that does not work.")
x=int(input('first number'))
y= int(input('second number'))
z = int(input('third number'))
p = int(input('exponent number'))
check_fermat(x,y,z,p)
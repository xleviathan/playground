def is_palindrome(arg):
    if arg[:] == arg[::-1]:
        return True
    else:
        return False
def gcd(a,b):
     if a > b :
         r= a%b

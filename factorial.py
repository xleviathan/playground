def factorial(n):
    if not isinstance(n,int):
        return None
    if n == 0 or n ==1 :
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))
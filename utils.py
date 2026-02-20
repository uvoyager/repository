def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def is_prime(n):
    ans=True
    for i in range(2, n**0.5+1):
        if n % i == 0:
            ans = False
            break
    return ans
def nsd(a, b):
    if b>a:
        a, b = b, a
    while b>0:
        a, b = b, a%b
    return a
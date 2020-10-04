def factorial(n):
    fact_tmp = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2,n+1):
            fact_tmp = fact_tmp*i
        return fact_tmp

def fibonacci(n):
    if n == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(1,n):
            tmp = a + b
            a = b
            b = tmp
        return b
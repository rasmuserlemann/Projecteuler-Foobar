import math
from operator import mul
from functools import reduce

def prime_factors(n):
    res = set()
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.add(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.add(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.add(n)
    return res

def totient(n):
    if n == 1: return 1
    return int(round(n * reduce(mul, [1 - 1.0 / p for p in prime_factors(n)])))

      
sum = 0
stop = 1000000
for k in range(2,stop+1):
    sum = sum + totient(k)

print(sum)
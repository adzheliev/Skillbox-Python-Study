from typing import List
from sympy import isprime

print(list(filter(lambda x: isprime(x), range(1000))))

primes: List = []
for i in range(1000):
    if isprime(i):
        primes.append(i)

print(primes)

'''На самом деле пока хорошо читаются оба решения, но если ещё усложнить функцию, то lambd'у будет читать сложно'''


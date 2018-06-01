import math as m

def last_prime(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def least_multiple(k):
    N = 1
    limit = m.sqrt(k)
    for i in last_prime(k):
        if i < limit:
            a = int(m.log(k) / m.log(i))
        else:
            a = 1
        N = N * (i) ** a
        i += 1
    print (N)
    return (N)
    
least_multiple(20)

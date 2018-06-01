import math as m

"""""" This function returns the list of primes up to n """""""""
def prime_list(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

""""" This function return and prints a number (integer) that can be divided by each nmber that is >= k and give a whole number.
def least_multiple(k):
""""" Starting point of multiplication """"""
    N = 1
""" Limit variable allows us to later decide on which primes need to be expanended (возвести в степень)
    limit = m.sqrt(k)
    for i in prime_list(k):
        if i < limit:
            a = int(m.log(k) / m.log(i))
        else:
            a = 1
        N = N * (i) ** a
        i += 1
    print (N)
    return (N)
    
least_multiple(20)

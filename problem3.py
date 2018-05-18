n = 600851475143
primes = []

factors = list(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

 
for num in factors:
  if all(num % i for i in range(2, num)) == True:
   primes.append(num)
    
print (primes[-1])

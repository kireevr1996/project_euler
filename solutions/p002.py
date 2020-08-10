fib_n = [1,2]
even_n = []
stop = 0

while stop < 4000000 :
  new_n = fib_n[-1]+fib_n[-2] 
  fib_n.append(new_n)
  stop = new_n
  
for nums in fib_n :
  if nums%2 == 0:
    even_n.append(nums)
  
print (sum(even_n))

for_sum = []

for i in range(1,1000):
  if i%3==0 or i%5==0:
    for_sum.append(i)
    
print (sum(for_sum))

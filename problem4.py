pal = []

for i in range(100,1000):
  for ii in range(100,1000):
    aa = i * ii
    a = str(aa)
    length_a = len(a)
    beg = a[0]+a[1]+a[2]
    end = a[-1]+a[-2]+a[-3]
    if beg == end:
      pal.append(int(a))
    
print (max(pal))

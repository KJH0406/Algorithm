x = int(input())

k =1
while x > k:
    x -= k
    k += 1
    
if k % 2 == 0:
    a = x
    b = k - x + 1
else:
    a = k - x + 1
    b = x
    
print(a, '/', b, sep='')
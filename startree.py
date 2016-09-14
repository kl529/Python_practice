
a = int(input())
b = "*"
c = " "


for i in range(1,a+1): print( (a-i)*" " + "*"*(2*i-1) )

for i in range(a):
  print( (a-i-1)*c  + b*(2*i+1))


for i in range(1,a+1):
    print(i*b)
   
   
for i in range(a-1,-1,-1):
    print(" "*i + (a-i)*b)
    
    
for i in range(a,-1,-1):
    print(b*i)
    
    
for i in range(a):
    print(i*" "+ (a-i)*b)
    

for i in range(1,a+1):
    print((a-i)*c + (2*(i) - 1)*b )
    
    
for i in range(a,0,-1):
    print((a-i)*c + (2*(i)-1)*b )
    
    
for i in range(1,a+1):
    print(c*(a-i) + b*((i*2) -1))
for k in range(a-1,0,-1):
    print(c*(a-k) + b*((k*2) -1))
    
    
for i in range(1,a+1):
    print(b*i + c*((a-i)*2) + b*i)


for k in range(a-1,0,-1):
    print(b*k + c*((a-k)*2) + b*k)
    
    
for i in range(a,0,-1):
    print(c*(a-i) + b *(2*i-1))

for k in range(2,a+1):
    print((a-k)*c + b*(2*k-1))
    
    
for i in range(1,a+1):
    print(c*(a-i)+b*i)
for k in range(a-1,0,-1):
    print(c*(a-k)+b*k)
    
    
for i in range(1,a+1):
    print(b*i)
    
for k in range(a-1,0,-1):
    print(b*k)

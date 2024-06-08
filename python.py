n=5
for i in range(1,n+1):
    for j in range(n-1):
        print(" ",end=' ')
    c=1
    for j in range(1,i+1):
        print(c,' ',sep=' ',end="  ")
        c=c*(i-j)//j
    print()
0/p:-  1    
        1    1    
        1    2    1    
        1    3    3    1    
        1    4    6    4    1  
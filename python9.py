r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        if i==1 or j==1 or i==r or i==j:
            print("$",end=' ')
        else:
            print(' ',end=" ")
    print()
o/p:-
$ 
$ $ 
$   $ 
$     $ 
$ $ $ $ $ 
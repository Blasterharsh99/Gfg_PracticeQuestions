n = int(input())
m = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
x = int(input())
y = int(input())

l,r = 0,0
while(l!=x and r!=y ):
    if( a[l][r+1]==1) and r<y:
        r+=1





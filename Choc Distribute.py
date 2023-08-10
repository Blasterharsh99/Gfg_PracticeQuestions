n=int(input())
m=int(input())
a=list(map(int,input().split()))
def min_diff(a,m,n):
    if(m==0 or n==0):
        return 0
    a.sort()
    if(n<m):
        return -1
    min_diff=a[n-1]
    i=0
    while(i+m-1<n):
        diff = a[i+m-1]-a[i]
        if min_diff>diff:
            min_diff=diff
        i+=1

    return min_diff

print(min_diff(a,m,n))
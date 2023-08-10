st=list(map(int,input().split()))
l=""
for i in st:
    l+=str(i)
rl=l[::-1]
h=[]
for i in rl:
    h.append(int(i))

print(h)

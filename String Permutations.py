from itertools import permutations

s=input()
n=len(s)
p=permutations(s)
for i in p:
    l=""
    for r in range(n):
        l+=i[r]
    print(l,end=" ")

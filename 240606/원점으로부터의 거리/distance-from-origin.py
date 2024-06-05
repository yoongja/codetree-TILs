from functools import cmp_to_key

n=int(input())
lst=[]
for i in range(n):
    a,b=tuple(map(int,input().split()))
    dis=abs(a)+abs(b)
    lst.append((a,b,i+1,dis))

lst.sort(key=lambda x:x[3])

for a,b,i,dis in lst:
    print(i)
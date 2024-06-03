n,k,t=tuple(map(str,input().split()))
n,k=int(n),int(k)
lst=[]
for i in range(n):
    lst.append(input())
result=[]
for i in lst:
    if i[:len(t)]==t:
        result.append(i)
result.sort()
print(result[k-1])
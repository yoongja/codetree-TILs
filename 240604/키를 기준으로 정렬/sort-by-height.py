n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(str,input().split())))

lst.sort(key=lambda x: x[1])
for i in lst:
    print(' '.join(i))
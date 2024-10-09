n = int(input())
lst = list(map(int,input().split()))

for i in range(n):
    minimum = i
    for l in range(i,n):
        if lst[l]<lst[minimum]:
            minimum=l
    temp = lst[i]
    lst[i] = lst[minimum]
    lst[minimum] = temp 

for i in lst:
    print(i,end=' ')
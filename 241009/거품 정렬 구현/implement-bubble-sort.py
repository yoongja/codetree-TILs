n = int(input())
lst = list(map(int,input().split()))

for l in range(n-1):
    for i in range(n-1):
        if lst[i]>lst[i+1]:
            sub = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = sub

for x in lst:
    print(x,end=' ')
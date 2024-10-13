n = int(input())
lst = list(map(int,input().split()))


for i in range(1,len(lst)):
    target = lst[i]
    j = i-1
    while(j>=0 and lst[j]>target):
        lst[j+1] = lst[j]
        lst[j] = target
        j-=1


for _ in lst:
    print(_,end=" ")
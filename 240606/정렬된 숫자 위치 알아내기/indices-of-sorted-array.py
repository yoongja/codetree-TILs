n= int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    lst[i]=(lst[i],i+1)
lst.sort(key=lambda x:x[0])
for i in range(len(lst)):
    lst[i]+=(i+1,)
lst.sort(key=lambda x:x[1])
for x,y,z in lst:
    print(f"{z}",end=" ")
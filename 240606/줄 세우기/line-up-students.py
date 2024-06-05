n= int(input())
lst=[]
for i in range(n):
    lst.append(tuple(map(int,input().split())))
    lst[i]+=(i+1,)

lst.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
for h,w,n in lst:
    print(f"{h} {w} {n}")
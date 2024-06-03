n=int(input())
lst=list(map(int,input().split()))
lst.sort()
for i in lst:
    print(i,end=" ")
print()
lst.sort(reverse=True)
for i in lst:
    print(i,end=" ")
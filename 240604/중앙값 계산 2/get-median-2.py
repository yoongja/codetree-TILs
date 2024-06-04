n= int(input())
lst = list(map(int,input().split()))
sub=[]
result=[]
for i in range(1,n+1,2):
    sub=lst[:i]
    sub.sort()
    print(sub[len(sub)//2],end=" ")
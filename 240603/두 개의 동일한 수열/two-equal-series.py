import sys
n=int(input())
lst_1=list(map(int,input().split()))
lst_2=list(map(int,input().split()))
lst_1.sort()
lst_2.sort()
for i in range(n):
    if lst_1[i]!=lst_2[i]:
        print("No")
        sys.exit()
print("Yes")
from itertools import combinations

ability = list(map(int, input().split()))

comb = list(combinations(ability,3))

min_val = 1e15 

arr = []
for c in comb:
    now = sum(c)
    arr.append(now)

arr.sort()

print(abs(arr[0]-arr[1]))
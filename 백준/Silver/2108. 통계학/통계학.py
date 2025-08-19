import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()
counts = Counter(nums)

print(round(sum(nums)/n))
print(nums[n//2])

most_common = counts.most_common(2)
if len(most_common) == 1:
    print(most_common[0][0])
elif most_common[0][1] == most_common[1][1]:
    print(most_common[1][0])
else:
    print(most_common[0][0])

print(nums[-1]-nums[0])
    
A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)
nums = [0 for _ in range(10)]

for r in result:
    nums[int(r)] += 1

for num in nums:
    print(num)

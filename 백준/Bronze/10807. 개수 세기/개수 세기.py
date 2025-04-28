n = int(input())
input_data = list(map(int, input().split()))
k = int(input())
count = 0

for i in input_data:
    if i == k:
        count += 1

print(count)
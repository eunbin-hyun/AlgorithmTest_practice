data_list = []
for i in range(10):
    data = int(input())
    data_list.append(data)

result = []
for i in data_list:
    result.append(int(i%42))

res = set(result)
print(len(res))
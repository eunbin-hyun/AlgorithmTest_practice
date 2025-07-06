x,y,w,h = map(int, input().split())

result = min(x-0, w-x, y-0, h-y)
print(result)
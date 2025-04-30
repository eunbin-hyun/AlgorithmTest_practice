dice = list(map(int, input().split()))
result = 0

if dice[0] == dice[1] == dice[2]:
    result = 10000 + dice[0]*1000 
elif (dice[0] == dice[1]) or (dice[2] == dice[1]):
    result = 1000 + dice[1]*100
elif (dice[0] == dice[2]):
    result = 1000 + dice[2]*100
else:
    result = max(dice)*100
    
print(result)
N, M = map(int, input().split())

cards = list(map(int, input().split()))
card_list =[]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = cards[i]+cards[j]+cards[k]
            if card_sum <= M:
                card_list.append(card_sum)

print(max(card_list))
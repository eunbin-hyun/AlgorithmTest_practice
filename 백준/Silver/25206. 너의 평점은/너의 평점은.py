result = 0
div = 0
for _ in range(20):
    subject, num, grade = input().split()
    score = {'A+' : 4.5, 'A0': 4.0, 'B+': 3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
    if grade == 'P':
        continue
    result += (float(num)*score[grade])
    div += float(num)

if result == 0:
    print(float(result))
else:
    result = result / div 
    print(result)
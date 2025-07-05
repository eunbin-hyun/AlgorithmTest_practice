while True:
    input_num = int(input())
    
    if input_num == -1:
        break
    
    num_list = []
    for i in range(1, input_num):
        if input_num % i == 0:
            num_list.append(i)
            
    if sum(num_list) == input_num:
        print(f"{input_num} =", end= ' ')
        for j in range(len(num_list)-1):
            print(f"{num_list[j]}" , end= ' + ')
        print(num_list[-1])
            
    else:
        print(f"{input_num} is NOT perfect.")
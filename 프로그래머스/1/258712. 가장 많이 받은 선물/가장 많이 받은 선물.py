def solution(friends, gifts):
    n = len(friends)
    present_dict = {}
    arr = [[0]*n for _ in range(n)]
    give_take = [[0, 0] for _ in range(n)]
    future = [0] * (n)
    
    for i in range(len(friends)):
        present_dict[friends[i]] = i
    
    for ar in gifts:
        A, B = ar.split()
        a_num = present_dict[A]
        b_num = present_dict[B]
        
        arr[b_num][a_num] += 1
        give_take[a_num][1] += 1
        give_take[b_num][0] += 1
        
    for i in range(n-1):
        for j in range(i+1, n, 1):
            if arr[i][j] > arr[j][i]:
                future[j] += 1
            elif arr[i][j] < arr[j][i]:
                future[i] += 1
            else:
                i_num = give_take[i][1] - give_take[i][0]
                j_num = give_take[j][1] - give_take[j][0]
                    
                if i_num > j_num:
                    future[i] += 1
                elif i_num < j_num:
                    future[j] += 1
    
    max_val = max(future)
    #print(future)
    #print(present_dict)
    #print(arr)
    #print(give_take)
    return max_val
        
def solution(brown, yellow):
    total_cnt = brown + yellow
    
    for x in range(3, int((total_cnt)/3) + 1, 1):
        #print(x, end = " ")
        y = total_cnt/x
        #print(y)
        if y%1 == 0 and x >= y and y >= 3:
            if 2*x + 2*(y-2) == brown and (x-2)*(y-2) == yellow:
                return [int(x), int(y)]
        
    

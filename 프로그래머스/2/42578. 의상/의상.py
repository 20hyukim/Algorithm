from collections import defaultdict

def solution(clothes):
    
    ddict = defaultdict(int)
    
    for a, types in clothes:
        ddict[types] += 1
    
    answer = 1
    #print(ddict)
    for v in ddict.values():
        answer *= (v+1)
        
    
    return answer - 1
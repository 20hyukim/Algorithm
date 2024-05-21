def solution(priorities, location):
    answer = 0
    
    while priorities:
        max_p = max(priorities)
        popped = priorities.pop(0)
        
        if popped != max_p:
            priorities.append(popped)
        
        else:
            answer += 1
            if location == 0:
                break
        
        location -= 1
        if location < 0:
            location = len(priorities) - 1
        
    return answer
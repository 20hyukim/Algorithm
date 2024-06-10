from collections import defaultdict

def solution(genres, plays):
    album = defaultdict(list)
    set_album = set(genres)
    length = len(genres)
    answer = []
    
    for a in set_album:
        album[a].append(0)
        
    for i in range(length):
        album[genres[i]][0] += plays[i]
        album[genres[i]].append(i)

    
    sorted_album = sorted(album.items(), key=lambda item:item[1][0], reverse=True)
    
    for genre, values in sorted_album:
        lists = []
        for i in range(1, len(values), 1):
            lists.append([plays[values[i]], values[i]])
        sorted_lists = sorted(lists, key=lambda x: (-x[0], x[1]))
        
        l = len(sorted_lists)
        if l > 2:
            l = 2
        for k in range(0, l):
            answer.append(sorted_lists[k][1])
        
    
    return answer
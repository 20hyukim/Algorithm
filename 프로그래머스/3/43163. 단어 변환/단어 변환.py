def solution(begin, target, words):
    def DFS(begin, words, cnt):
        nonlocal min_step
        if begin == target:
            # print(target)
            if cnt < min_step:
                min_step = cnt
                return
        l = len(begin)

        for w in words:
            diff = 0
            for i in range(l):
                if w[i] != begin[i]:
                    diff += 1
            if diff == 1:
                words.remove(w)
                DFS(w, words, cnt + 1)
                words.append(w)

    min_step = len(target) + 2
    if target not in words:
        return 0
    DFS(begin, words, 0)
    if min_step == len(target) + 2:
        return 0

    return min_step

for i in range(int(input())):
    total = []
    for i in range(int(input())):
        total.append(list(map(int, input().split())))

    total.sort()
    passed = len(total)
    highest_interview_rank = len(total) + 1
    for paper, interview_rank in total:
        if highest_interview_rank < interview_rank:
            passed -= 1
            continue
        highest_interview_rank = interview_rank

    print(passed)

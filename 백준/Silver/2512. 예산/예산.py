import math

def budget(requests, limit_budget):
    avg = limit_budget / len(requests)
    revisit = []
    assigned = []

    for request in requests:
        if request <= avg:
            limit_budget -= request
            assigned.append(request)

        else:
            revisit.append(request)

    if revisit == requests:
        return int(avg)
    return budget(revisit, limit_budget)




input()
requests = list(map(int, input().split()))
limit_budget = int(input())
if sum(requests) <= limit_budget:
    print(max(requests))
else:
    print(budget(requests, limit_budget))
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_truck = [0] * bridge_length
    curr_weight = 0

    while truck_weights or bridge_truck:
        answer += 1

        if bridge_truck:
            curr_weight -= bridge_truck.pop(0)

        if truck_weights:
            if curr_weight + truck_weights[0] <= weight:
                popped = truck_weights.pop(0)
                bridge_truck.append(popped)
                curr_weight += popped
            else:
                bridge_truck.append(0)

    return answer
from collections import deque


head_location = [0, 0]
tail_location = deque()
tail_location.append([0, 0])
n = 0
snake_location = []
apples = []
queue_direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])


def print_squares(n, square):
    for i in range(n):
        print(square[i])
    print()

def place_apples(apple_num):
    global apples, n
    apples = [[0] * n for _ in range(n)]
    for _ in range(apple_num):
        i, j = map(int, input().split())
        apples[i - 1][j - 1] = 1

    return apples


def mark_directions(n):
    directions = []
    for _ in range(n):
        s, d = input().split()
        directions.append([int(s), d])

    return directions

def go_straight(seconds, direction):
    global head_location, tail_location, snake_location, apples, n
    passed_seconds = 0
    #print("seconds")
    #print(seconds)
    #print()

    for i in range(seconds):

        head_location = [head_location[0] + direction[0], head_location[1] + direction[1]]
        passed_seconds += 1
        tail_location.append(head_location)

        if not (0 <= head_location[0] < n and 0 <= head_location[1] < n):
            return False, passed_seconds
        if snake_location[head_location[0]][head_location[1]] == 1:
            return False, passed_seconds

        snake_location[head_location[0]][head_location[1]] = 1
        if not apples[head_location[0]][head_location[1]]:
            #print("tail_location")
            #print(tail_location)
            #print()
            x, y = tail_location.popleft()
            snake_location[x][y] = 0

        else:
            apples[head_location[0]][head_location[1]] = 0

        #print("snake_location")
        #print_squares(n, snake_location)

        #print("apple_location")
        #print_squares(n, apples)

        #print("tail_location")
        #print(tail_location)
        #print()

        #print("head_location")
        #print(head_location)
        #print()

        #print("passed_seconds")
        #print(passed_seconds)

    return True, seconds

def change_direction(lr):
    global queue_direction

    if lr == 'D':
        queue_direction.append(queue_direction.popleft())
        return queue_direction[0]
    queue_direction.appendleft(queue_direction.pop())
    return queue_direction[0]


def duration_game(directions):
    global head_location, tail_location, snake_location, apples, n
    seconds = 0
    direction = [0, 1]

    while directions:
        #print("directions: ", directions)
        next_s, next_d = directions.pop(0)
        #print("next_s:", next_s)
        #print("next_d:", next_d)

        succeeded, passed_seconds = go_straight(next_s - seconds, direction)

        #print("succeeded:", succeeded)
        #print("passed_seconds:", passed_seconds)

        if succeeded:
            seconds += passed_seconds
            direction = change_direction(next_d)
        else:
            seconds += passed_seconds
            return seconds

    succeeded, passed_seconds = go_straight(n+1, direction)

    return seconds + passed_seconds





if __name__ == "__main__":
    n = int(input())
    snake_location = [[0] * n for _ in range(n)]
    snake_location[0][0] = 1
    apples = place_apples(int(input()))
    directions = mark_directions(int(input()))
    print(duration_game(directions))
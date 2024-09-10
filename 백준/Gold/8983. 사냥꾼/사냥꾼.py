def get_animal_location(n):
    animals = []

    for i in range(n):
        animal = list(map(int, input().split()))
        animals.append(animal)
    return animals


def find_animal_in_range(l, r, xs, m):
    left = 0
    right = m-1

    while left <= right:
        mid = (left + right) //2
        if l <= xs[mid] <= r:
            return 1

        elif l > xs[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return 0


def find_animals_in_range(l, n, animals, xs, m):
    for animal in animals:
        d = l - animal[1]
        animal[1] = d

    #print(animals)
    xs.sort()
    total = 0
    for x, d in animals:
        if d < 0:
            continue
        total += find_animal_in_range(x-d, x+d, xs, m)

    return total


if __name__ == "__main__":
    m, n, l = map(int, input().split())
    xs = list(map(int, input().split()))
    animals = get_animal_location(n)
    #print("animals:", animals)
    print(find_animals_in_range(l, n, animals, xs, m))
def get_animal_location(n):
    animals = []

    for i in range(n):
        animal = list(map(int, input().split()))
        animals.append(animal)
    return animals


def find_animal_in_range(l, r, xs):
    for x in xs:
        if l <= x <= r:
            return 1

    return 0
def find_animals_in_range(l, n, animals, xs):
    for animal in animals:
        d = l - animal[1]
        animal[1] = d

    #print(animals)

    total = 0
    for x, d in animals:
        if d < 0:
            continue
        total += find_animal_in_range(x-d, x+d, xs)

    return total


if __name__ == "__main__":
    m, n, l = map(int, input().split())
    xs = list(map(int, input().split()))
    animals = get_animal_location(n)
    #print("animals:", animals)
    print(find_animals_in_range(l, n, animals, xs))
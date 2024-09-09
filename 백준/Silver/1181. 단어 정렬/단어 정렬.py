def sort_words(n):
    words = set()
    for i in range(n):
        words.add(input())

    words = list(words)
    words = sorted(words, key=lambda a: (len(a), a))

    for w in words:
        print(w)


if __name__ == "__main__":
    sort_words(int(input()))
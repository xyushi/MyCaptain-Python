def most_frequent():
    s = input()
    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1 
        else:
            counter[char] = 1
    print(sorted(counter.items(), key=lambda x : x[1], reverse = True))
most_frequent()

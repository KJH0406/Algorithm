while True:
    n = int(input())
    if n != 0:
        word_list = []
        lower_list = []
        for i in range(n):
            k = input()
            lower_word = k.lower()
            lower_list.append(lower_word)
            word_list.append(k)

        lower_list.sort()

        for item in word_list:
            if lower_list[0] == item.lower():
                print(item)
    else:
        break
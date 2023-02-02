N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
words_res = set(words)
words_res = list(words_res)
words_res.sort()
words_res.sort(key = len)

# for j in range(len(words_res)-1 , 0, -1): 
#     for k in range(j):
#         if len(words_res[k]) > len(words_res[k+1]):
#             words_res[k], words_res[k+1] = words_res[k+1], words_res[k]

for m in range(len(words_res)):
    print(words_res[m])

n = int(input())
p_sequence = [1] * 200
for i in range(4, n + 1):
    p_sequence[i] = p_sequence[i - 3] + p_sequence[i - 1]
print(p_sequence[n])
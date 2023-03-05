row_dic = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
column_dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
delta = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}
K, D, N = input().split()
N = int(N)
move = [input() for _ in range(N)]
K_si, K_sj = row_dic[K[1]], column_dic[K[0]]
D_si, D_sj = row_dic[D[1]], column_dic[D[0]]

for i in range(N):
    di, dj = delta[move[i]]
    ni, nj = K_si + di, K_sj + dj
    if K_si == D_si and K_sj == D_sj:
        if 0 <= ni < 8 and 0 <= nj < 8:
            K_si, K_sj = ni, nj
    else:
        if 0 <= ni < 8 and 0 <= nj < 8 and ni == D_si and nj == D_sj:
            if 0 <= D_si + di < 8 and 0 <= D_sj + dj < 8:
                K_si, K_sj = ni, nj
                D_si, D_sj = D_si + di, D_sj + dj

        elif 0 <= ni < 8 and 0 <= nj < 8:
            if ni != D_si or nj != D_sj:
                K_si, K_sj = ni, nj

final_king_i = ''
final_king_j = ''
final_d_i = ''
final_d_j = ''

for key, value in column_dic.items():
    if value == K_sj:
        final_king_j += key
    if value == D_sj:
        final_d_j += key
for key, value in row_dic.items():
    if value == K_si:
        final_king_i += key
    if value == D_si:
        final_d_i += key

print(final_king_j + final_king_i)
print(final_d_j + final_d_i)






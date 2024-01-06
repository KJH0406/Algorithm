h, w = map(int, input().split())  # H: 높이, W, 너비
blocks = list(map(int, input().split()))  # 블록 배열

max_h = blocks[0]  # 가장 높은 블록 높이
max_idx = 0  # 가장 높은 블록 인덱스
before_h = blocks[0]  # 이전 블록 높이
ans = 0  # 빗물의 양

bucket = 0 # 임시 양동이

res = [0] * w

for i in range(1, w):
    current_h = blocks[i]  # 현재 블록 높이

    # 가장 높은 블록 보다 높은 블록을 만났을 때
    if max_h < current_h:
        if i - 1 != max_idx:
            for j in range(i - 1, max_idx, -1):
                res[j] = max_h - blocks[j]
            bucket = 0
        max_h = current_h
        max_idx = i

    # 가장 높은 블록과 동일한 블록을 만났을 때
    elif max_h == current_h:
        for j in range(i, max_idx, -1):
            res[j] = max_h - blocks[j]
        bucket = 0
        max_idx = i

    # 낮은 블록 들을 만났을 때
    else:
        if current_h > before_h:

            for j in range(i-1, max_idx, -1):
                if current_h - blocks[j] > 0:
                    res[j] = current_h - blocks[j]
                else:
                    break

    before_h = current_h

print(sum(res))


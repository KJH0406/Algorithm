n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]

room.sort(key=lambda x: (x[1], x[0], abs(x[0] - x[1])))
start = room[0][0]
end = room[0][1]


room = room[1:]
cnt = 1

for ns, ne in room:
    if end <= ns:
        start, end = ns, ne
        cnt += 1

print(cnt)

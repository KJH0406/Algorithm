N, K = map(int, input().split())
Male = [0] * 7
FeMale = [0] * 7
final_room = []

for _ in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        Male[Y] += 1
    else:
        FeMale[Y] += 1

while Male:
    room = Male.pop()
    if room <= K and room != 0:
        final_room.append(room)
    else:
        if room != 0:
            Male.append(K)
            Male.append(room-K)
while FeMale:
    room = FeMale.pop()
    if room <= K and room != 0:
        final_room.append(room)
    else:
        if room != 0:
            FeMale.append(K)
            FeMale.append(room-K)
            
print(len(final_room))

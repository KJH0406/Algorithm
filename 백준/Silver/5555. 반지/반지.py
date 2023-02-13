ring = input()
T = int(input())
count = 0
for i in range(T):
    alpha_list = input()
    for j in range(len(alpha_list)-len(ring)+1):
        if alpha_list[j:j+len(ring)] == ring:
            count += 1
            break
    else:
        for j in range(len(alpha_list)-len(ring)+1, len(alpha_list)):
            if alpha_list[j:] + alpha_list[:abs(len(alpha_list)-len(ring)-j)] == ring:
                count += 1
                break

print(count)
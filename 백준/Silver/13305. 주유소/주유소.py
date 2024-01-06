n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_price = cities[0]
res = 0

for i in range(len(roads)):
    road = roads[i]
    city = cities[i + 1]
    if min_price <= city:
        res += min_price * road
    else:
        res += min_price * road
        min_price = city
print(res)





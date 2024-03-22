def dfs(routes, answer, visited, current_city, ticket_count):
    answer.append(current_city)

    # 모든 티켓을 사용했으면 경로 반환
    if len(answer) == ticket_count + 1:
        return answer

    if current_city in routes:
        # 인덱스와 도시 이름 enumerate 사용
        for i, city in enumerate(routes[current_city]):
            # 방문한 적이 없는 도시 확인
            if not visited[current_city][i]:
                visited[current_city][i] = True
                # 재귀 호출로 다음 도시 탐색
                result = dfs(routes, answer, visited, city, ticket_count)
                if result:
                    return result  # 올바른 경로 찾음

                # 잘못된 경로인 경우 이전 상태로 복원(백트래킹)
                visited[current_city][i] = False  # 방문 여부 초기화
                answer.pop()  # 탐색한 경로에서 제거


def solution(tickets):
    routes = {}
    visited = {}

    # 모든 티켓을 기준으로 경로와 방문 배열 생성
    for depart, arrive in tickets:
        if depart in routes:
            routes[depart].append(arrive)
        else:
            routes[depart] = [arrive]

        if depart in visited:
            visited[depart].append(False)
        else:
            visited[depart] = [False]

    # 각 경로별로 알파벳 순으로 정렬
    for route in routes.values():
        route.sort()

    return dfs(routes, [], visited, 'ICN', len(tickets))
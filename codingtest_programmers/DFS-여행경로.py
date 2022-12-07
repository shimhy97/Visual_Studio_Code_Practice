from collections import defaultdict, deque


def solution(tickets):
    
    ticketDict = defaultdict(lambda: [])
    
    # 그래프 만들기
    for ticket in tickets :
        O = ticket[0]
        D = ticket[1]
        ticketDict[O].append(D)
    
    # 알파벳 순으로 정렬
    for key,values in ticketDict.items():
        ticketDict[key] = deque(sorted(values))
    
    # 처음 출발지 선정
    dep = "ICN"
    stack = [dep]
    
    path = []
    
    # 순회하며 탐색 (DFS 방식)
    
    while stack : # 스택이 남아있는 동안 반복
        top = stack[-1]
        if len(ticketDict[top]) != 0: # top에서 출발하여 방문해야할 국가가 남아있다면
            stack.append(ticketDict[top].popleft()) # 목적지 국가 하나를 방문 대기열에 추가
        else : # top에서 출발하여 방문해야 할 국가가 남아있지 않은 경우
            path.append(stack.pop())  # stack에서 꺼내서 경로에 추가
            
    return path[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

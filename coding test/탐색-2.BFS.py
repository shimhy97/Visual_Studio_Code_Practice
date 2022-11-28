from collections import deque

visited = [False]*9
graph = [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

# 최상단 노드 탐색 (graph[1])
# 해당 노드를 큐에 올리기
# 해당 노드 방문 처리 ★

def BFS(graph,start,visited):
    queue = deque([start]) # 큐에 노드 삽입 ( 현재 위치 알아보기 위함 )
    visited[start]=True # 방문 정보 저장
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

BFS(graph,1,visited)
    
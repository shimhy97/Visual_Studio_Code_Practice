import os
import numpy as np
# 메모장의 그래프 정보를 불러오기

with open('C:\\Users\\shimh\\OneDrive\\바탕 화면\\Coding\\Visual_Studio_Code_Practice\\graph.txt','r') as file:
    lines = file.readlines()
    last_node = int(lines[-1][0])
    graph = {}
    for i in range(last_node+1):
        graph.setdefault(int(i),[])
    # print(lines)
    for line in lines:
        load = line.strip("\n").split()
        # print(load)
        a,b,c = int(load[0]),int(load[1]),int(load[2])
        # print(a,b,c)
     
        graph[a].append([b,c])



def find_shortest_path(graph,start,end):
    INF = int(1e9)
    last_node = len(graph)

    # 3개의 저장 빈 공간 필요. === 1.출발지부터 각 노드까지의 거리 저장 공간, 2.방문 정보 저장 공간, 3.경로 출력을 위한 이전 경로 저장 공간.
    distances={}
    visit_history = {}
    before_node = {}

    # 세개의 dictionary 초기화
    for i in range(last_node):
        distances.setdefault(int(i),INF)  #거리 저장 노드 생성, 모두 무한대로 초기화
        visit_history.setdefault(int(i),'not_visited') #방문 위치 노드 생성, 모두 "not_visited"로 초기화

    for i in range(last_node-1):    # 출발지는 이전 노드가 없기 때문에, 크기 -1
        before_node.setdefault(int(i+1),None) #이전 경로 저장 노드 / 연결 정보까지 저장하기 위해 딕셔너리 형태를 쓴다.

    distances[start]=0  # 출발지 ~ 출발지의 노드 거리 0으로 선정
    visit_history[start]='visited' # 출발 노드는 바로 방문 처리
    node = start  #출발 노드 설정
    
    #본격적인 작업
    while 'not_visited' in visit_history.values(): # 방문하지 않은 노드가 없을때까지 반복.

        for d in graph[node]:#이동한 노드에 대해서 또 반복 해야지. 근데 이제 여기선 cost를 비교하는 과정이 들어간다.
                             # 이때 d는 연결상태를 나타내는 원소 2개짜리 리스트이다. d[0],d[1]. 
                             # 예를들어 graph[4]는 4번 노드와 주변 노드와의 연결 정보를 알려준다.
                             # d[0]        d[1]
                             # 1번까지 거리 9,
                             # 2번까지 거리 6 
                             # 3번까지 거리 14, 
                             # 7번까지 거리 8을 의미한다.

            temp_distance = distances[node] + d[1]
            if temp_distance < distances[d[0]]:  # 현재 노드에서 다른 노드까지 가는 거리와 이미 저장되어 있는 거리 정보와 비교.
                distances[d[0]] = temp_distance  #더 짧은 경로가 있으면? 갱신.
                # visit_history[d[0]]='confirmed'
                before_node[d[0]] = node
                # print(distances[d[0]])

        min_distance = INF
        min_node = 0
        for j in graph:  #모든 노드를 돌며, 거리가 최소이면서 방문하지 않은 노드를 찾는 과정. 그 후 이 노드로 이동해야 하므로 노드 번호를 반환.
            if distances[j] < min_distance and visit_history[j]=='not_visited':
                min_distance = distances[j] 
                min_node = j

        node = min_node
        visit_history[node] = 'visited' # 이동


    trace = []
    n = end
    while n != start:
        trace.append(n)
        n = before_node[n]
    trace.append(start)
    trace.reverse()
    
    print("=================탐색 결과=================")
    print("{0}번 노드에서 각 노드까지의 거리는 다음과 같습니다.".format(start))
    print(distances)
    print("{0}번 노드에서 {1}번 노드까지 이동하는 경로는".format(start,end))
    for v in range(len(trace)-1):
        print(trace[v],"-> ",end='')
    print(trace[-1],"입니다.")


start,end = map(int,input("시작 노드와 끝 노드를 입력하세요 : ").split())
find_shortest_path(graph,start,end)
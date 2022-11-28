## 본 파일은 Myopic Algorithm에 사용되는 다익스트라 알고리즘 제작을 위해, v1의 내용을 개선함.

# 개선사항 (22/02/28) :
# read_graph 부분 함수화
# 경로 탐색 부분 삭제 --> 따라서 메인 함수 실행 부분에 end 변수가 빠짐


import os
import numpy as np
import pandas as pd
# 메모장의 그래프 정보를 불러오기

def read_graph(graph_file):
    with open(graph_file,'r') as file:
        lines = file.readlines()
        node_number = int(lines[-1].split()[0]) + 1
        graph = {}
        for i in range(node_number):
            graph.setdefault(int(i),[])
        # print(lines)
        for line in lines:
            load = line.strip("\n").split()
            # print(load)
            a,b,c = int(load[0]),int(load[1]),int(load[2])
            # print(a,b,c)

            graph[a].append([b,c])

    return graph,node_number

graph,node_number = read_graph('graph_figure6-11.txt')
# print(graph)

def find_shortest_path(graph,start):
    INF = int(1e9)
    # 3개의 저장 빈 공간 필요.
    distances={}        # 1.출발지부터 각 노드까지의 거리 저장 공간
    visit_history = {}  # 2.방문 정보 저장 공간, 
    before_node = {}    # 3.경로 출력을 위한 이전 경로 저장 공간.

    # 세개의 dictionary 초기화
    for i in range(node_number):
        distances.setdefault(int(i),INF)  #거리 저장 노드 생성, 모두 무한대로 초기화
        visit_history.setdefault(int(i),'not_visited') #방문 위치 노드 생성, 모두 "not_visited"로 초기화

    for i in range(node_number-1):    # 출발지는 이전 노드가 없기 때문에, 크기 -1
        before_node.setdefault(int(i+1),None) #이전 경로 저장 노드 / 연결 정보까지 저장하기 위해 딕셔너리 형태를 쓴다.

    # print(distances)
    distances[start]=0  # 출발지 ~ 출발지의 노드 거리 0으로 선정
    visit_history[start]='visited' # 출발 노드는 바로 방문 처리
    node = start  #출발 노드 설정
    
    #본격적인 알고리즘
    while 'not_visited' in visit_history.values(): # 방문하지 않은 노드가 없을때까지 반복

        for d in graph[node]:# d는 연결상태를 나타내는 원소 2개짜리 리스트이다. d[0],d[1]. 
                             # 예를들어 graph[4]는 4번 노드와 주변 노드와의 연결 정보를 알려준다.
                             # d[0]        d[1] 
                             # 1번까지 거리 9,
                             # 2번까지 거리 6 
                             # 3번까지 거리 14, 
                             # 7번까지 거리 8을 의미한다.

            temp_distance = distances[node] + d[1]
            if temp_distance < distances[d[0]]:  # 현재 노드에서 다른 노드까지 가는 거리 temp_distance와 
                                                 # 이미 저장되어 있는 거리 정보 distances[d[0]]와 비교.
                distances[d[0]] = temp_distance  #더 짧은 경로가 있으면? 갱신.
     
        min_distance = INF
        min_node = 0
        for j in graph:  #모든 노드를 돌며, 거리가 최소이면서 방문하지 않은 노드를 찾는 과정. 그 후 이 노드로 이동해야 하므로 노드 번호를 반환.
            if distances[j] < min_distance and visit_history[j]=='not_visited':
                min_distance = distances[j] 
                min_node = j

        node = min_node # 이동
        visit_history[node] = 'visited' 

    # print("=================탐색 결과=================")
    # print("{0}번 노드에서 각 노드까지의 최단거리는 다음과 같습니다.".format(start))
    # print(distances)
    return distances.values()

find_shortest_path(graph,0)

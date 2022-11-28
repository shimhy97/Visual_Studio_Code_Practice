# import Dijkstra as dijk
import pandas as pd
import numpy as np
import os
import Dijkstra_v2 as dijk



def make_dataframe_dijk(graph_file):    #각 노드에서 노드로 가는 최단거리 테이블 생성 d(i,j) 과정 (nxn matrix)
    dist_df = pd.DataFrame()
    graph,node_number = dijk.read_graph(graph_file)   # 그래프 읽어오기//텍스트 형식의 인접 리스트 넣어주면 그래프와 노드 수 가져옴      
    for start in range(node_number):                          # 최단거리 nxn matrix 가져오기.
        dist_df[start] = dijk.find_shortest_path(graph,start)      # 다익스트라 코드 재활용하여 반복함.
    dist_df.columns = [chr(i+65) for i in np.array(dist_df.columns)]  # 노드명 숫자로 되어있는데 알파벳으로 변환
    dist_df.index = dist_df.columns
    return dist_df, node_number

def make_dataframe_dijk_from_1_node(graph,start):    # facility의 위치를 받아 그 지점에 설치한 후 각 노드까지의 최단거리 테이블 반환하는 함수
    node_df = pd.DataFrame()                         # d(i,A) d(i,B) 등의 array 반환하며, shape는 n*1 일 것임.
    node_df = dijk.find_shortest_path(graph,start)
    return node_df

def make_dataframe_h_d(dist_df,node_df):              # sigma h_i * d_ij table 생성하는 함수
    print(dist_df)
    hd_df = pd.DataFrame(index=dist_df.index, columns = dist_df.columns)  #빈 데이터프레임 생성.
    for i in dist_df.columns:
        hd_df[i] = np.array(dist_df[i])*np.array(node_df).reshape(-1)     # node_df의 shape가 1*n이라 n*1로 바꿔줘야 해서 reshape
    
    sum_array = np.dot(dist_df,node_df).ravel() ## 첫번째 column별 SUM 결과
    return hd_df,sum_array

#input file 정의
graph_file = './graph_figure6-11.txt'     #그래프 TXT파일 위치 
dist_df,node_number = make_dataframe_dijk(graph_file)          #d(i,j) 테이블 생성
node_df = pd.read_excel('./Myopic_nodeInfoTable.xlsx', index_col = 0)   # 노드별 수요 저장 테이블

facility_array = []

hd_df, sum_array = make_dataframe_h_d(dist_df,node_df)

## myopic 알고리즘을 통해 최적의 노드 산출

index = np.where(sum_array == sum_array.min())[0][0]  # np.where로 가장 작은값의 인덱스를 불러오고, 거기서 index만 추출
facility_node = dist_df.columns[index]   # 첫번째 facility를 세울 노드의 위치를 반환함 이때 index는 order, columns는 알파벳임에 유의
facility_array.append(facility_node)     # 퍼실리티 건설 정보 저장

make_dataframe_dijk_from_1_node(graph_file,0)       # facility로부터 각 노드까지의 최단거리 테이블 생성.


## 비교




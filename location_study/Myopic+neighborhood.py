
import pandas as pd
import numpy as np
import os
import Dijkstra_v2 as dijk   # 다익스트라 모듈 (지난 과제 활용)

# Code by 심훈용 (2022.03.04)
# ============= 자주 활용되는 부분 함수 구현, 함수형 프로그래밍 =================

#지난 과제인 다익스트라 코드 활용하여 각 노드에서 노드로 가는 최단거리 테이블 생성 d(i,j) 과정 (nxn matrix)
def make_dataframe_dijk(graph_file):    
    dist_df = pd.DataFrame()
    graph,node_number = dijk.read_graph(graph_file)   # 그래프 읽어오기//텍스트 형식의 인접 리스트 넣어주면 그래프와 노드 수 가져옴      
    for start in range(node_number):                          # 최단거리 nxn matrix 가져오기.
        dist_df[start] = dijk.find_shortest_path(graph,start)      # 다익스트라 코드 재활용하여 반복함.
    dist_df.columns = [chr(i+65) for i in np.array(dist_df.columns)]  # 노드명 숫자로 되어있는데 알파벳으로 변환
    dist_df.index = dist_df.columns
    return dist_df, node_number

 # sigma h_i * d_ij table 생성하는 함수
def make_dataframe_h_d(dist_df,node_df):             
    # print(dist_df)
    hd_df = pd.DataFrame(index=dist_df.index, columns = dist_df.columns)  #빈 데이터프레임 생성.
    for i in dist_df.columns:
        hd_df.loc[i] = np.array(dist_df[i])*np.array(node_df).ravel()    # node_df의 shape가 1*n이라 일렬로 펴줘야 해서 ravel() 사용
    hd_df = hd_df.T   # 출력해보니까 뒤집어져 있었다. Transpose 해주자.
    sum_array = np.array(hd_df.sum())
    return hd_df,sum_array


## 거리 테이블을 받아 1개의 최적의 노드 산출하는 함수
def find_best_node(sum_array):
    index = np.where(sum_array == sum_array.min())[0][0]  # np.where로 가장 작은값의 인덱스를 불러오고, 거기서 index만 추출
    facility_node = dist_df.columns[index]   # 첫번째 facility를 세울 노드의 위치를 반환함 이때 index는 order, columns는 알파벳임에 유의
    return facility_node


# demand까지 곱한 테이블 생성
def find_min_dist(dist_df,itoN):
    df = pd.DataFrame(index=dist_df.index, columns = dist_df.columns)
    for i in range(node_number):
        a = np.array(dist_df.iloc[:,i])
        b = np.array(itoN)
        c = np.where(a<b,a,b)
        df.iloc[i]=c
    df = df.T
    return df

# 변수 정의 시작
iteration = 1   # 반복 연산을 위한 변수
facility_node_array = []  # 최적의 facility 결정되면 하나씩 위치 저장해놓는 리스트

#input file 정의
graph_file = './graph_figure6-11.txt'     #그래프 TXT파일 위치 
dist_df,node_number = make_dataframe_dijk(graph_file)   #d(i,j) 테이블 생성 및 노드 수 같이 가져옴
node_df = pd.read_excel('./Myopic_node_info_table.xlsx', index_col = 0)   # 노드별 수요 저장 테이블
original_dist_df = dist_df             # dist_df는 반복마다 새로 정의되지만 d(i,N) 때문에 원본도 하나 필요함
original_hd_df,original_sum_array = make_dataframe_h_d(dist_df,node_df) # 추후 활용


# =============Myopic Algorithm==============
while iteration <= 5:
    
    hd_df, sum_array = make_dataframe_h_d(dist_df,node_df)      # h*d table 및  sum array 반환
    facility_node = find_best_node(sum_array)            #최적의 노드 위치 (알파벳) 반환

    facility_node_array.append(facility_node)     # 퍼실리티 건설 정보 저장

    # I로부터 최단거리.
    itoN = original_dist_df[facility_node]

    # 두 dist_table 비교하여 min값 반환
    dist_df = find_min_dist(dist_df,itoN)
    iteration +=1

facility_node_array = sorted(facility_node_array)  # 알파벳 순 정렬
print("=====Myopic Algorithm 수행 결과=====")
print('시설 노드 = ',facility_node_array) ##

non_facility_node_array = list(set(node_df.index) - set(facility_node_array))   #시설이 설치되지 않은 노드
print('시설이 설치되지 않은 노드 = ', non_facility_node_array)

neighbor_group = {}

for i in facility_node_array:   # 그룹 지정할 빈 변수 설정. dictonary 안에 list 들어있는 형태.
    neighbor_group[i] = []

#============= Neighborhood Groups 생성=============
for i in non_facility_node_array:  # L E C K H B D

    temp_for_index=np.array([])
    temp_for_find_group=np.array([])
    for j in facility_node_array:  # I G F J A
        temp_for_index = np.append(temp_for_index , j)
        temp_for_find_group = np.append(temp_for_find_group , original_dist_df.loc[i,j])  
    
    index = np.where(temp_for_find_group == min(temp_for_find_group))[0][0]
    val = temp_for_index[index]

    neighbor_group[val].append(i)

print("=====facility와 neighborhood-group 관계는 다음과 같습니다. =====")
print(neighbor_group)


#============= Neighborhood Alogorithm=============
while True:
    upgraded_facility_array=[]
    for k,v in neighbor_group.items():
        # array = neighbor_group[i] 
        sum_array={}
        A = set(k)
        B = set(v)
        union = A|B
        for node in union:  # 그룹 내의 모든 노드들에 대해
            result = 0  
            key = node      # facility를 돌려가면서 세워 본다
            items = union - set(key)
            for item in items:      # facility 임시로 세우고, 안세운 애들에 대해 
                result += original_hd_df.loc[item,key]      # facility로 가는 h_d 합계를 계산한다.
            sum_array[key] = result             # 그리고 그 결과를 저장.

        fact = min(sum_array.values())

        min_node = list(sum_array.keys())[list(sum_array.values()).index(fact)]  ## neighborhood 내부에서 가장 최적의 facility 위치를 출력해줌.
        upgraded_facility_array.append(min_node)

    if upgraded_facility_array == facility_node_array:    # 개선이 없다면 끝냄
        break
    else:
        facility_node_array = upgraded_facility_array     # 개선이 있다면, upgrade 반영하고 다시 반복
        continue

print("=====최종 결과===== ")
print(facility_node_array)
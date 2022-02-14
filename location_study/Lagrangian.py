import numpy as np
import pandas as pd

graph = np.array(
    [
        [0,8,15,10,21,26],
        [8,0,12,7,16,23],
        [15,12,0,19,9,11],
        [10,7,19,0,11,17],
        [21,16,9,11,0,13],
        [26,23,11,17,13,0]
    ]
)
demand = np.array([10,8,22,18,7,55])
distance = 10
P = 2
alpha = 2
inf = 1e9
iteration = 0
alpha_iteration = 0
upper_bound=[]
lower_bound=[]
zero_array = [0]*6
max_iteration = 4


a_ij = np.where(graph<=10,1,0)
X_list = np.array([1,1,0,0,0,0])
# print(a_ij)

# X_j column 
def find_X_j(series):

    arr1 = list(series)
    arr2 = np.zeros(6)
    while True:
        L = arr1.index(max(arr1))
        arr2[L]=1
        if arr2.sum()==2:
            break
        arr1[L]=-inf
      
    return arr2

#LB column
# X_j가 배정됨에 따라 커버되는 new_Zi 를 구하는 것은 그냥 a_ij의 i 번째 행을 갖다 쓰면 된다..
def find_LB(df):
    arr=[]
    for n,i in enumerate(df['X_j']):
        if i==1:
            sigma = np.dot(a_ij[n],df['h_i'])
            arr.append(sigma)
        elif i==0:
            arr.append(0)
    return arr
    
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

# Dataframe 생성
# column_list = ['h_i','lambda_i','Z_i','(h_i-lambda_i)*Z_i','sigma(a*lambda)','X_j','sigma(a*lambda)X_j','sigma(aX)','sigma(aX)-Z','LB']
index_list = ['A','B','C','D','E','F']
table = np.zeros((len(index_list),1))

df = pd.DataFrame(table)
df.index = index_list
# df.columns=column_list

#초기값 생성
df['h_i'] = demand
h_bar = df['h_i'].mean()
df['lambda_i']=np.array([h_bar+0.5*(i-h_bar) for i in df['h_i']])
df['Z_i']= np.where(df['h_i']-df['lambda_i']>=0,1,0)
df['(h_i-lambda_i)*Z_i'] = (df['h_i']-df['lambda_i'])*df['Z_i']
df['sigma(a*lambda)'] = np.dot(a_ij,df['lambda_i'])
df['X_j'] = find_X_j(df['sigma(a*lambda)'])
df['sigma(a*lambda)X_j'] = df['sigma(a*lambda)']*df['X_j']
df['sigma(aX)']= np.dot(a_ij,df['X_j'])
df['sigma(aX)-Z']=df['sigma(aX)']-df['Z_i']
df['LB']=find_LB(df)
df['zero_array']=zero_array

upper_bound.append((df['(h_i-lambda_i)*Z_i']+df['sigma(a*lambda)X_j']).sum())
lower_bound.append(df['LB'].max())
UB = min(upper_bound)
LB = max(lower_bound)

#t 생성
t_n = alpha*(UB-LB)/sum((df['sigma(aX)-Z']**2))
#1st iteration 종료 -------
print("초기값 df:", df)

#iteration을 통한 새로운 df 생성. -------
#lambda_i+1
def find_next_sheet(df):
    s1=df['zero_array']
    s2=df['lambda_i']-t_n*df['sigma(aX)-Z']
    s3=pd.concat([s1, s2],ignore_index=True, axis=1).max(axis=1)
    df['lambda_i']=s3
    df['Z_i']= np.where(df['h_i']-df['lambda_i']>=0,1,0)
    df['(h_i-lambda_i)*Z_i'] = (df['h_i']-df['lambda_i'])*df['Z_i']
    df['sigma(a*lambda)'] = np.dot(a_ij,df['lambda_i'])
    df['X_j'] = find_X_j(df['sigma(a*lambda)'])
    df['sigma(a*lambda)X_j'] = df['sigma(a*lambda)']*df['X_j']
    df['sigma(aX)']= np.dot(a_ij,df['X_j'])
    df['sigma(aX)-Z']=df['sigma(aX)']-df['Z_i']
    df['LB']=find_LB(df)
    return df

def find_next_bound(df):
    upper_bound.append((df['(h_i-lambda_i)*Z_i']+df['sigma(a*lambda)X_j']).sum())
    lower_bound.append(df['LB'].unique().sum())
    UB = min(upper_bound)
    LB = max(lower_bound)
    return UB,LB

# print(upper_bound,lower_bound)
# print(t_n)

# iteration
while abs(LB-UB)>0.1 and alpha < 00.1 and alpha_iteration<max_iteration:
    alpha_iteration +=1  # 요게 max가 되면 계산 종료
    iteration +=1
    df=find_next_sheet(df)  # df 갱신
    UB_new, LB_new = find_next_bound(df) # bound 갱신
    # while True:     # iteration을 계속 진행할지, 아니면 alpha를 바꿀지를 결정하는 단계
    if UB_new < UB :  # 좋아지면?
        alpha_iteration = 0 # 알파 카운팅횟수 초기화
        t_n = alpha*(UB-LB)/sum((df['sigma(aX)-Z']**2))
        UB,LB  = UB_new,LB_new     # UB, LB 값 더 좋아졌으니 Best 값 갱신
        print(UB,LB)
    elif UB_new >= UB or alpha_iteration == max_iteration: # 안좋아지면?
        alpha *=0.5
        t_n = alpha*(UB-LB)/sum((df['sigma(aX)-Z']**2))
        print(UB,LB)

print(df)

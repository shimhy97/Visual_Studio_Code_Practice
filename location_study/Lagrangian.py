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
distance = 10  #covering distance
P = 2   # number of facilities
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
#find t_n, step size
def find_t_n(df):
    t_n = alpha*(UB-LB)/sum((df['sigma(aX)-Z']**2))
    return t_n

#display option
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

# Create Dataframe
index_list = ['A','B','C','D','E','F']
table = np.zeros((len(index_list),1))

df = pd.DataFrame(table)
df.index = index_list

#초기 Dataframe 생성
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


#iteration을 통한 새로운 df 생성. -------
#lambda_i+1
def find_next_sheet(df,t_n):
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

# iteration
while abs(LB-UB)>1 and alpha > 0.1 and alpha_iteration<max_iteration:
    
    if iteration >=1:   # 처음엔 그냥 보낸다.
        df=find_next_sheet(df,t_n)  # df 갱신   # lambda, Zn, (h-lambda).....(sigma_aij - Z )
        UB, LB = find_next_bound(df) # bound 갱신

    while UB_temp >= UB and iteration >= 1:     # alpha 값을 유지한 채 iteration을 계속 진행할지, 아니면 alpha를 바꿀지를 결정하는 단계
                            # 안좋아지면, 알파값을 계속 절반으로 만드는 단계이다.
        alpha_iteration+=1
        alpha *=0.5
        t_n_temp = find_t_n(df) # t_n 갱신
        df_temp = find_next_sheet(df,t_n_temp)
        UB_temp, LB_temp = find_next_bound(df_temp)
        print("{0}-{1}. UB가 좋아지지 않아 alpha를 갱신합니다.".format(iteration,alpha_iteration))
        print("alpha 값은 {0} 입니다".format(alpha))

    #t_n 갱신
    t_n = find_t_n(df)

    alpha_iteration = 0 
    iteration +=1
    if iteration == 1 :
        print("1번째 초기값입니다.")
    elif iteration >=2 :
        print("{0}번째 반복입니다. UB가 개선되었습니다.".format(iteration))
    print("LB:{0},UB:{1:.3f},alpha:{2:.3f},t_n:{3:.3f}".format(LB,UB,alpha,t_n))
    print(df)
    print("---------------------------------------------------")


print("-----FINAL_RESULT-----")
print("LB:{0},UB:{1:.3f},alpha:{2:.3f},t_n:{3:.3f}".format(LB,UB,alpha,t_n))
print(df)
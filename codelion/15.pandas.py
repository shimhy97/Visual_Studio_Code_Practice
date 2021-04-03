# 요일별 사망교통사고 시각화
import pandas as pd
from IPython.display import display
import numpy as np
import matplotlib as plt
data = pd.read_csv('C:\\Users\\shimh\\Downloads\\Traffic_Accident_2017.csv', encoding='euc-kr')
display(data)

time_df = data['발생년월일시'].astype('str').str[-2:].value_counts()  # 데이터에서 발생년월일시 열의 끝 두자리의 갯수에 대해 분석

time_df = time_df.sort_index()

time_df = time_df.index.astype('int32')


bins = [-1,2,5,8,11,14,17,20,24]   # 앞에있는 수 초과, 뒤에있는 수 이하의 범위로 쪼갠다.
labels = ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23']

cat = pd.cut(time_df.values,bins,labels=labels)

display(cat)

pd.dataframe(cat)


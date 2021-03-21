N,M=map(int,input().split())
array=[]
min_value_list=[]
for i in range(N):
    array.append(list(map(int,input().split())))
    min_value_list.append(min(array[i]))

final = max(min_value_list)

print(final)

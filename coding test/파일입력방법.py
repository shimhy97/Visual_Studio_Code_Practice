# 정렬 알고리즘

array = [7,5,9,0,3,1,6,2,4,8]
new_array = []

for i in range(len(array)):
    new_array.append(min(array))
    array.remove(min(array))


print(new_array)


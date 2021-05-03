# # 정렬 알고리즘

# array = [7,5,9,0,3,1,6,2,4,8]
# new_array = []

# for i in range(len(array)):
#     new_array.append(min(array))
#     array.remove(min(array))
# print(new_array)


# #2차원 리스트 초기화 하는법
# m = 6
# n = 4 
# array = [ [0]*m for i in range(n)]
# print(array)

# array[0][1]=1

# print(array)

# # 리스트에서 특정 원소 삭제 하는 법
# lili = [1,3,5,6,3,6,7,4,7,4,8,3,8,1]
# remove_set= [1,5]

# removed = [ i for i in lili if i not in remove_set]
# print(removed)

# import math
# maximum = int(input())
N = list(range(2,100))
i=2
while i < 10:
    n=2
    while i*n <= max(N):
        try:    
            N.remove(i*n)
            n+=1
        except:
            n+=1
            continue
    i+=1

print(N)



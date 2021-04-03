import numpy as np

array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)

print(array1)
print(array2)

array3 = np.concatenate([array1,array2], axis=0)
print(array3, array3.size, array3.shape)


# ///////////배열 나누기

array = np.arange(8).reshape(2,4)
left, right = np.split(array,[2], axis=1)  # 2*4 배열의 index=2인 열!!!(axis=0 이면 행, axis=1이면 열을 의미함.) 을 기준으로 나눠라.
print(left)
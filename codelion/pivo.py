# 피보나치 수열
def Pivonacci(n):
  arr= [0]*n
  arr[0]= 1
  arr[1]= 1
  for i in range(2,n):
    arr[i] = arr[i-2] + arr[i-1]
  print(arr)
Pivonacci(7)
N,M,K= map(int,input().split())

array = list(map(int,input().split()))

array= sorted(array)
count = 0
sum = 0

for i in range(M):
    if (i+1) % K == 0 :
        sum+=array[-2]
    else:
       sum +=array[-1]



print(sum)
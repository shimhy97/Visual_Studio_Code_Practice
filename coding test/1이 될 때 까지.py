# N,K= map(int,input().split())

N,K = 100,3
count=0
while N != 1:
    if N % K != 0:
        N = N-1
    else:
        N = N / K
    count+=1

print(count)
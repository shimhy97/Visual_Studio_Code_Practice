S = list(map(int,input()))
result=0
for i in len(S)-1:
    start = S[i]
    if temp == 0:
        temp = S[i]+S[i+1]
    else:
        temp = S[i]*
N=5
count=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if str(3) in str(i) or str(3) in str(j) or str(3) in str(k):
                count+=1

print(count)
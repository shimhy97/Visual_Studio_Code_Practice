N = int(input())

direction = list(input().split())

(x,y) = (1,1)
(tx,ty) = (1,1)
for i in direction:
    if i == 'U':
        tx = x-1
    if i == 'D':
        tx = x+1
    if i == 'L':
        ty = y-1
    if i == 'R':
        ty = y+1
    # 논리 체크하는 부분!
    if tx == 0 or tx == N+1 or ty == 0 or ty==N+1:
        continue
    x,y = tx,ty

print(x,y)    
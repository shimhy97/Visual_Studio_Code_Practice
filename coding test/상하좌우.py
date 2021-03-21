
# -------------

orders = ["U"]*10
location = [1,1]
control=["L","R","U","D"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for order in orders:
    for i in range(len(control)):
        if order == control[i]:
            nx = location[0]+dx[i]
            ny = location[1]+dy[i]
    if nx<1 or nx >5 or ny <1 or ny>5:
        continue
    location[0],location[1] = nx,ny

print(location)
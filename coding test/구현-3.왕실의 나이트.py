location = list(input())

location[1] = ord(location[1])-ord('a')+1
location = [int(i) for i in location]
(X,Y) = tuple(location)

delta_x = [-2,-1,1,2]
delta_y = [-2,-1,1,2]
attempt=0

for dx in delta_x:
    for dy in delta_y:
        (X_n,Y_n)=(X+dx,Y+dy)
        if abs(dx)==abs(dy) or X_n<1 or X_n>8 or Y_n<1 or Y_n>8:
            continue
        else:
            attempt+=1

print(attempt)

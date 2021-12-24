size = list(map(int,input().split()))
location = list(map(int,input().split()))
island = [list(map(int, input().split())) for _ in range(size[0])]

print(size, location, island)

history=[]
count=1
history.append([location[0],location[1]])

def turn_left(direction):
    if direction==0: #North, 왼쪽은 West 방향
        return 3
    elif direction==1: # East
        return 0
    elif direction==2: #South
        return 1
    elif direction==3: # West
        return 2

def move(direction,location): # 이동하는 함수. 방향과 현재 위치를 받아
    if direction==0: #North
        location[0]-=1
        return location
    elif direction==1: # East
        location[1]+=1
        return location
    elif direction==2: #South
        location[0]+=1
        return location
    elif direction==3: # West
        location[1]-=1
        return location

def move_back(direction,location): # 이동하는 함수. 방향과 현재 위치를 받아 이동 후의 위치 표시
    if direction==0: #North
        location[0]+=1
        return location
    elif direction==1: # East
        location[1]-=1
        return location
    elif direction==2: #South
        location[0]-=1
        return location
    elif direction==3: # West
        location[1]+=1
        return location

while True:
    
    i=location[0]
    j=location[1]
    k=location[2]

    k = turn_left(k)
    
    [i,j] = move(k,[i,j])
    if [i,j] in history or island[i][j]==1 or i<0 or i>=size[0] or j<0 or j>=size[1]: #회전만, 로케이션 변동 없음
        location[2]=k
        continue

    
    if [i,j] not in history and island[i][j]==0 : #경로 안가본 곳 or 육지 
        location = [i,j,k] # 현재위치를 이동한 위치로변경
        history.append(location[:2]) #방문한 장소 추가
        count+=1 # 이동 횟수 증가
    else: # 뒤로 가기
        location = move_back(k,location[:2]) 
        if island[location[0]][location[1]]==1:
            break
            


print(count)


'''Description
step (move)
action
checkSafeorNot
getScopeMap
getSoldierStatusMap
stateSoldier <-경비병의 상태 list
'''

from itertools import compress
def getScopeMap(secureInfoDB,distance): # 감시범위 Map 생성
    
    scopeMap = ['안전'] * (distance + 1)
    
    for n, soldierIndex in enumerate(secureInfoDB) :
        scope_d = min(soldierIndex[0])
        scope_u = max(soldierIndex[0])
        mask = scopeMap[scope_d : scope_u + 1]
        scopeMap[scope_d : scope_u + 1] = [(n,'위험') for i in range(len(mask))]
    
    return scopeMap
    # scopeMap[n] = '안전'
    # scopeMap[m] = (병사번호,'위험')

def getSoldierStatusMap(secureInfoDB,distance):
    
    statusMap = []
    for soldierIndex in secureInfoDB:
        location = 0
        workTime = soldierIndex[1][0]
        breakTime = soldierIndex[1][1]
        period = workTime + breakTime
        oneSoldierDB = [0]
        
        
        while location < distance :
            oneSoldierDB  = oneSoldierDB + ['근무']*workTime + ['휴식']*breakTime
            location += period
        statusMap.append(oneSoldierDB)
        
    return statusMap

def solution(distance, scope, times):
    elapsedTime = 0
    secureInfoDB = []
    secureInfoDB = list(zip(scope,times))
    
    #동일 경비병에 대해 감시범위, 근무지도 추가
    
    # secureInfoDB[0] = (scopeInterval,timeInterval) = ([3,4],[2,5]) = 경비병의 정보
    # secureInfoDB[0][0] = (scopeInterval,timeInterval) = [3,4] = 경비병의 근무범위
    # secureInfoDB[0][1] = (scopeInterval,timeInterval) = [2,5] = 경비병의 근무시간 정보
    scopeMap = getScopeMap(secureInfoDB,distance)
    statusMap = getSoldierStatusMap(secureInfoDB,distance)
    
    # process
    while elapsedTime < distance :
        elapsedTime += 1
        # check in danger zone
        if scopeMap[elapsedTime] =='안전':
            continue
        # check soldier is in working state
        workingSoldierIndex = scopeMap[elapsedTime][0]
        if statusMap[workingSoldierIndex][elapsedTime] == '휴식':
            continue
        # 근무중인 경비병에게 붙잡힘
        break
        
    answer = elapsedTime
    print("최대 도달 거리",answer)
    return answer



distance = 10
scope = [[3,4], [5, 8]]
times = [[2, 5], [4, 3]]
answer = solution(distance,scope,times)
print(answer)
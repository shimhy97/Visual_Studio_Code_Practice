from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def search(name):
    search_queue = deque() #새 큐를 생성
    search_queue += graph["you"] #모든 이웃을 탐색 큐에 추가
    searched = []

    while search_queue: #큐가 비어 있지 않는 한 계속 실행
        person = search_queue.popleft() #큐의 첫 번째 사람을 꺼냄
        if not person in searched:
            if person_is_seller(person): #망고 판매상인지 확인
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person] #망고 판매상이 아니면 모든 이웃을 탐색 목록에 추가
                searched.append(person)
    return False #망고 판매상이 아무도 없다.

def person_is_seller(name):
    return name[-1] == 'm'

search("you")
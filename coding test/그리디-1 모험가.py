# num = int(input())
# array = list(map(int,input().split()))

from collections import deque


num = 5
array = [3]*100
array.sort(reverse=True)

order = 0
count = 0

delta = array[0]
count += 1 
while True:
    order += delta
    if order < len(array):
        delta = array[order]
        count +=1
    else:
        print(count)
        break
        

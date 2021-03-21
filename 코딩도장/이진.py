def binary_search(list,item):
  
  low = 0
  high = len(list)-1
  while True:
    mid = (low + high) // 2
    if item == list[mid] :
      return list[mid]
      break
    elif item < list[mid]:
      high = mid
      continue
    elif item > list[mid]:
      low = mid
      continue




test_list = [1,3,5,7,9]
print("결과")
print( binary_search(test_list, 3) )
def solution(lottos, win_nums):
    answer = []
    ##로또 번호 일치 갯수 확인 로직
    ##0의 갯수 확인 로직
    correctNum = len (set(lottos) & set(win_nums))
    zeroNum = lottos.count(0)

    poor = correctNum
    rich = correctNum + zeroNum

    # 등수 계산 로직
    #0~1개 = 6등
    #그 후 추가시마다 등수 1계단씩 상승
    poor = 7 - poor if poor != 0 else 6
    rich = 7 - rich if rich != 0 else 6

    answer = [rich,poor]

    ##0의 갯수 파악 로직
    
    return answer
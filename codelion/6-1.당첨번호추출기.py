
import random

while True:
    try: 
        buy = int(input("로또 몇개 살래?"))
        for i in range(buy):
            lotto = random.sample(range(1,45),6)
            print(sorted(lotto))
        break
    except:
        print("숫자만 입력하세요")
        continue


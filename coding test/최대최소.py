# a,b = map(int, input("숫자 두개를 입력하세요").split())

a,b = 1000,255
big = max(a,b)
small = min(a,b)

print(a,b)


def LGfunction(a,b):

    while a<=b:
        b -=a
        if (b==1):
            return b
        elif(b==0):
            return a    
    return LGfunction(b,a)


print(LGfunction(big,small))    
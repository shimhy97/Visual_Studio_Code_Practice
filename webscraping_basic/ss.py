a = int(input("초 입력: "))
hour =  a//3600
minute = (a % 3600) // 60
second = a % 60
print(hour,"시",minute,"분", second,"초")

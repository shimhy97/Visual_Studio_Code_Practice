import requests
import os

logic_start = True
reset = True

while logic_start == True:
    print("Welcome to IsItDown.py!")
    url = input("Please write a URL or URLs you want to check. seperated by comma\n")

    url = url.split(',')

    count=0
    for i in url:
        i = i.strip()
        if 'https://' not in i:
            url[count] = 'https://'+ i 
        else:
            url[count] = i
        count +=1
    print(url)
        
    for i in url:
        try:
            x = requests.get(i)
            print(i,"is up!")
        except:
            print(i,"is down!")

    

    while reset == True:
        Y_or_N = input("Do you want to start over? y/n\n")
        if Y_or_N == "y":
            os.system("cls")
            break
        elif Y_or_N == "n":
            print("K, bye!")
            logic_start = False
            break
        else:
            print("try again. That is not Answer..")
            continue

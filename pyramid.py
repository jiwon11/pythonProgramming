num = int(input('출력 줄 수 입력 : '))

for i in range(num):
    for k in range(num,i,-1):
        print(' ',end='')

    for k in range((i+1)*2-1):
        print("*",end='')
    print()
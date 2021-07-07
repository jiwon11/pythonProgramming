studentNumber = input('학번 :')
name = input('이름: ')
firstNum = int(input('첫번째 수: '))
secondNum = int(input('두번째 수: '))
str1 = studentNumber+name
print(str1[0],str1[1],str1[2],str1[3],str1[4],str1[5],str1[6],str1[7],str1[8],str1[9],str1[10],str1[11])
print(str1[-1],str1[-2],str1[-3],str1[-4],str1[-5],str1[-6],str1[-7],str1[-8],str1[-9],str1[-10],str1[-11],str1[-12])
print(str1[firstNum:secondNum])
fruitList = []

while True:
  menu = input('삽입/삭제/종료 : ')
  if menu == '종료':
    break
  elif menu == '삽입':
    fruit = input('과일 이름 : ')
    fruitList.append(fruit)
    print(fruitList)
  elif menu == '삭제':
    if len(fruitList) > 0:
      delFruit = fruitList.pop(0)
      print('삭제된 과일 : ',delFruit)
      print(fruitList)
    else:
      print('삭제할 과일이 없습니다.')
  else:
    print('잘못 입력하였습니다!!!')
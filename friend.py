#!/usr/bin/env python
# -*- coding: utf-8 -*-

friendList = []
while True:
  print('****************')
  print("1. 이름 추가\n2. 이름 삭제\n3. 이름 수정\n4. 종료")
  menu = input('메뉴 선택 : ')
  if menu == '1':
    name = input('이름 : ')
    if name in friendList:
      print('이미 있는 이름')
    else:
      friendList.append(name)
      print(friendList)
  elif menu == '2':
    name = input('이름 : ')
    if name in friendList:
      friendList.remove(name)
      print(friendList)
    else:
      print('해당 이름은 없음')
  elif menu == '3':
    name = input('이름 : ')
    if name in friendList:
      newName = input('새이름 : ')
      friendList[friendList.index(name)] = newName
      print(friendList)
    else:
      print('해당 이름은 없음')
  elif menu == '4':
    break

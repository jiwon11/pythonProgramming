#!/usr/bin/env python
# -*- coding: utf-8 -*-

dogList = []

for i in range(3):
  dog = {}
  dog['name'] = input('강아지 이름 :') 
  dog['age'] = int(input('강아지 나이 :'))
  dog['kind'] = input('강아리 종류 :')
  dogList.append(dog)

print('리스트내용')
for i in dogList:
  print(dogList.index(i),'번째 :', i)

print('나이가 3살 이상인 강아지')
for dog in dogList:
  if (dog['age'] >= 3):
    print(dog)
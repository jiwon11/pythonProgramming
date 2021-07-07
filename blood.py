#!/usr/bin/env python
# -*- coding: utf-8 -*-

bloodList = []
bloodType = ['a', 'b', 'ab', 'o']

num = 0
while num < 10:
  blood = input('헌혈한 헐액형(a, b, ab, o) : ')
  if blood not in bloodType:
    print('혈액형 오류 !!!')
  else:
    bloodList.append(blood)
    num = num + 1

print('저장된 혈액형')
for b in bloodList:
  print(b, end=' ')
print()

print('A 혈액형 수 : ', bloodList.count('a'))
print('B 혈액형 수 : ', bloodList.count('b'))
print('AB 혈액형 수 : ', bloodList.count('ab'))
print('O 혈액형 수 : ', bloodList.count('o'))
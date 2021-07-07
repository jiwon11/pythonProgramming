set1 = {'x', 'b', 'g', 'd', 'q' }
set2 = {'b', 'w', 'g', 'q', 'o' }

print('set1= ', set1)
print('set2= ', set2)

print('set1 ∪ set2=', set1 | set2)
print('set1 ∩ set2=', set1 & set2)
print('set1 - set2=', set1 - set2)
print('set2 - set1=', set2 - set1)
print('set1 ^ set2=', set1 ^ set2)

char1 = input('영문자 한자 입력 :')
if char1 in set1:
  print('중복')
else:
  set1.add(char1)
  print('set1= ', set1)

char2 = input('영문자 한자 입력 :')
if char2 in set2:
  set1.remove(char2)
  print('set2= ', set2)
else:
  print('삭제할 문자가 없습니다.')
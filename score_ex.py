from score import total, ave, grade, output, max_student

ban = []

for i in range(5):
  student = []
  name = input('성명 : ')
  student.append(name)
  language = int(input('국어점수 : '))
  student.append(language)
  english = int(input('영어점수 : '))
  student.append(english)
  math = int(input('수학점수 : '))
  student.append(math)
  ban.append(student)

for student in ban:
  student.append(total(student))
  student.append(ave(student))
  student.append(grade(student))
  print(output(student))

for i in range(4):
  print(f'{i}명 학생 비교')
  if i == 0:
    maxStudent = max_student()
    if maxStudent == None: print('비교할 학생이 없음')
  elif i == 1:
    print(output(max_student(ban[1])))
  elif i == 2:
    print('성적이 더 좋은 학생')
    print(output(max_student(ban[2], ban[4])))
  elif i == 3:
    print('성적이 가장 좋은 학생')
    print(output(max_student(ban[1], ban[2], ban[3])))
def total(student):
  total = 0
  for i in range(1,4):
    total += student[i]
  return total

def ave(student):
  total = 0
  for i in range(1,4):
    total += student[i]
  ave = round(total / 3 ,2)
  return ave

def grade(student):
  ave = student[5]
  if ave >= 90:
    grade = 'A'
  elif ave >= 80 and ave < 90:
    grade = 'B'
  elif ave >= 70 and ave < 80:
    grade = 'C'
  elif ave>= 60  and ave < 70:
    grade = 'D'
  else:
    grade = 'F'
  return grade

def output(student):
  output = f'{student[0]} : 국어:{student[1]} 영어:{student[2]} 수학:{student[3]} 총점:{student[4]} 평균:{student[5]} 학점:{student[6]}'
  return output

def max_student(*student):
  if len(student) == 0:
    return None
  else:
    total = 0
    maxStudent = []
    for i in range(len(student)):
      if total < student[i][4]:
        total = student[i][4]
        maxStudent = student[i]
    return maxStudent

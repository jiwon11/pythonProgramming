password = '0516'

count=0
while True:
  if count <3:
    input_password = input('비밀번호 입력 : ')
    if input_password == password:
      print("로그인 되었습니다!")
      break
    elif input_password != password:
      print("비밀번호를 다시 입력하세요.")
  else:
    print("로그인 실패! 횟수초과!")
    break
  count += 1

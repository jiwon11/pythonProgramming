key = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(password):
  global key
  encode = ''
  for char in password:
    if key.index(char)+2 >= len(key):
      encode += key[(key.index(char)+2)%len(key)]
    else:
      encode += key[key.index(char)+2]
  return encode

def decrypt(password):
  global key
  decode = ''
  for char in password:
    if key.index(char)-2 <= 0:
      decode += key[(key.index(char)-2)%len(key)]
    else:
      decode += key[key.index(char)-2]
  return decode

with open('password.txt', 'w') as file:
  for i in range(3):
    password = input('문자열 입력(대문자, 빈칸, 특수기호 불가) : ')
    file.write("%s \n" %(encrypt(password)))

with open('password.txt', 'r') as file:
  for password in file: 
    stripPassword = password.strip()
    print(f'암호 : {stripPassword}')
    print(f'해독 : {decrypt(stripPassword)}')
file.close()
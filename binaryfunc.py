def binary(n):
  global binList
  if (n == 0): return 0
  elif (n > 1): binary(n // 2)
  bin = n % 2
  binList.append(str(bin))
  return bin
  


while True:
  binList = []
  num = int(input('양의 정수 입력(음수 입력시 종료) : '))
  if num == -1 :
    break
  else:
    bin = binary(num)
    print(f'{num}의 이진수 : {"".join(binList)}   binary() 함수 반복횟수 : {len(binList)}')


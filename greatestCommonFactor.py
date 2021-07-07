def gcd(first,second, *nums):
  numList = [first, second] + list(nums)
  minNum = min(numList)
  i = 1
  stack = []
  while i <= minNum:
    split = []
    for num in numList:
      if (num % i == 0): 
        split.append(True)
    if split.count(True) == len(numList): 
      stack.append(i)
    i += 1
  return max(stack)
  
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))
num4 = int(input('정수4 입력 : '))
print(f'{num1}, {num2}의 최대공약수 : {gcd(num1, num2)}')
print(f'{num1}, {num2}, {num3}의 최대공약수 : {gcd(num1, num2, num3)}')
print(f'{num1}, {num2}, {num3}, {num4}의 최대공약수 : {gcd(num1, num2, num3, num4)}')
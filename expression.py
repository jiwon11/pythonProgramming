def convertExp(exp):
  expStack = []
  convert = ''
  for i in exp:
    if i.isdigit() == True:
      convert += i
    else:
      if (i == '(' or i == '+' or i == '-' or i == '*' or i == '/') :
        expStack.append(i)
      elif (i == ')'):
        while expStack[-1] != '(':
          convert += expStack.pop()
        expStack.pop()
  return convert

exp1 = '((8-6)*(4+(9/3)))'
exp2 = '((9*2)-(3*((2+5)/7)))'
exp3 = '((9*2)-((3*(2+5))/7))'

print(exp1, '=', convertExp(exp1))
print(exp2, '=', convertExp(exp2))
print(exp3, '=', convertExp(exp3))
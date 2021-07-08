from BankAccountClass import BankAccount

ba1 = BankAccount('김철수', 30000)
ba2 = BankAccount('이영희')

ba1.display()
ba2.display()
print()

print(f'{ba1.getName()} 150000입금/50000출금')
ba1.deposit(150000)
ba1.display()
ba1.withdraw(50000)
ba1.display()
print()

print(f'{ba2.getName()} 50000입금/100000출금')
ba2.deposit(50000)
if ba2.withdraw(100000) == False:
  print('예금 부족!!!')
  ba2.display()
else:
  ba2.display()
print()

print('이자계산후')
ba1.calcuInterest()
ba1.display()
ba2.calcuInterest()
ba2.display()
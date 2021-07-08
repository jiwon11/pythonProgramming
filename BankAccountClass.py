class BankAccount:
  INTEREST = 0.05
  def __init__(self, name, balance = 0):
    self.__name = name
    self.__balance = balance

  def deposit(self, sum):
    self.__balance += sum
  
  def withdraw(self, sum):
    if self.__balance >= sum:
      self.__balance -= sum
      return True
    else:
      return False

  def getName(self):
    return self.__name
  def getBalance(self):
    return self.__balance
  def calcuInterest(self):
    self.__balance += int(self.__balance * BankAccount.INTEREST)
  def display(self):
    print(f'name : {self.getName()} balance : {self.getBalance()}')
  
class Calculator():
  def add(self, num1,num2):
     return num1+num2
     
 
  def subtract(self, num1,num2):
    return num1-num2
  
  def multiply(self, num1, num2):
    return num1*num2
 
  def devide(self, num1, num2):
    if num2 ==0:
           return 0
    return num1/num2  

if __name__ == "__main__":

     calculator = Calculator() 
     print(calculator.add(1,3))
     print(calculator.subtract(3,1))
     print(calculator.multiply(3,1))
     print(calculator.devide(4,2))

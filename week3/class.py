''' 1
class a:
    def __init__(self):
        self.text = " "
    def getString(self):
        self.text = input("Enter a string: ")
    def printString(self):
        print(self.text.upper())

if __name__=="__main__":
    b = a()
    b.getString()
    b.printString()
'''

''' 2
class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        return self.length ** 2
square = square(5)
print("Square area is ", square.area())
'''

''' 3 
class shape:
    def area(self):
        return 0
class rect(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectangle = rect(4, 6)
print("Rectangle Area:", rectangle.area()) 
'''

''' 4 
import math

class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y 
    def show(self):
        print(f"coordinates of points: ({self.x}, {self.y})")  
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def dist(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y) **2)

p1 = point(3, 4)
p2 = point(6, 8)
p1.show()  
p2.show() 
print(p1.dist(p2))  
'''

''' 5 
class account:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance 
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Current balance: ${self.balance}")
        else:
            print("error")
    def withdraw(self, amount):
        if amount>self.balance:
            print("Withdrawal failed")
        elif amount>0:
            self.balance-=amount
            print(f"successful transfer. Current balance: ${self.balance}")
        else:
            print("error.")

acc =account("John Doe", 100)
print(f"account owner: {acc.owner}")
print(f"initial balance: ${acc.balance}")

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  
'''

''' 6
def prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
numbers =[10, 3, 5, 8, 13, 17, 21, 29, 31, 42]
prime = list(filter(lambda x: prime(x), numbers))
print("Prime numbers:", prime)
'''
# self: Là tham số mặc định của class tức là khi khai báo 1 hàm bất kì bắt buộc phải có self
class Student: # Quy tắc chữ cái đầu của class phải in Hoa
    def __init__(self, name, age, address):
        self.names = name
        self.ages = age
        self.address = address
    def show_info(self):
        print(f"Name: {self.names} - Age: {self.ages} - Address: {self.address}")
        
    # dunder __ methods
    def __str__ (self):
        return f"<Student(name={self.names}, age={self.ages})>"

    def __gt__(self, other):
        return self.ages > other.ages
            
""" student_one = Student("Bob", 23)
student_two = Student("Marry", 25)
print(student_one > student_two) """

student_one = Student("Bob", 23, "New York")
#student_one.show_info()
Student.show_info(student_one)

# Kế thừa: Inheritance
class Human:                         #Class: Cha
    def __init__(self, name):
        self.name = name

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name) # super() : ở đây là lời gọi đến class Human
        self.age = age
    def __str__(self) -> str:
        return f"Name: {self.name}, age: {self.age}"
    
student_two = Student("Joe", 33)
print(student_two)

# Example: The CreditCard Class
class CreditCard:
    """A consumer credit card."""
    def __init__ (self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero

        customer the name of the customer
        bank     the name of the bank
        acnt     the acount identifier
        limit    credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self): # Lấy ra
        """ Return name of the customer."""
        return self._customer
    
    def get_bank(self): # Lấy ra
        """ Return the bank's name."""
        return self._bank
    
    def get_account(self): # Lấy ra
        """ Return the card identifying number (typically stored as a string)."""
        return self._account
    
    def get_limit(self): # Lấy ra
        """ Return current credit limit."""
        return self._limit
    
    def get_balance(self): # Lấy ra
        """ Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

if __name__ == '__main__': # Terminilogy testing , câu điều kiện test
    wallet = []
    wallet.append(CreditCard('John Bowma', 'CS', '51323', 2500))
    wallet.append(CreditCard('John Bowma', 'CF', '51322', 3500))
    wallet.append(CreditCard('John Bowma', 'CK', '51321', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()
# Operator - Overloading
class GFG: 
    def __init__(self, val): 
        self.val = val 
          
    def __add__(self, val2): 
        return GFG(self.val + val2.val) 
  
obj1 = GFG("Geeks") 
obj2 = GFG("ForGeeks") 
obj3 = obj1 + obj2 
print(obj3.val)


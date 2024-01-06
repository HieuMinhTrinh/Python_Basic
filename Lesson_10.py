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


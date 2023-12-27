# values
# data types
# input

# numbers: 1,2,3,-1,0... (integers: so nguyen); 1.25, 3.14, 0.00(float)
# string: "hello", 'man'
# boolean: True False

print(type(1)) # int
print(type(1.25)) # float
print(type('')) # str
print(type(True)) # bool

# variables

x = 5
print(type(x)) # int
x = 6
print(x)

_ = 45
print(_)

#input => tra ve 1 str

fullname = input("enter your name: ")
print(f"My name's",fullname) 

number = int(input("Enter your number: "))
print(type(number))

# Operators
# + - * / // ** %
print(1 + 2) # Shift + Alt + Bottom
print(1 - 2)
print(3 * 2)
print(3 / 2) # float
print(3 // 2) # int
print(5 ** 2) # Lũy thừa
print(4 % 2) # Lấy phần dư

# >, <, >=, <=, ==, !=
# bool - True/False

print(1 > 2) # False
print(1 < 3) # True
print(3.0 == 3) # Về mặt kiểu dữ liệu là khác nhau nhưng về mặt GIÁ TRỊ là giống nhau => True
print('a' != 'a') # False

# and0 - or - not

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# Bôi đen tất cả giống nhau: Ctrl + shift + L
#                       hoặc Ctrl + D
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

print(bool(0)) # False
print(bool(1)) # Khác 0 thì True
print(1 and 2) # Kết quả 2
print(1 and 0) # Kết quả 0
print(0 or 2) # Kết quả 2
print(1 or 2) # Kết quả 1

#Cmt nhanh(bỏ cmt): Ctrl + /

# falsy: 0, 0.0, 0j, None: No value
# list: []
# set: set()
# dict: {}
# tuple: ()

print(bool({})) # False

print(1+2)
"""
+ set   # - Được tạo bởi dấu {} và không thể chứa các phần tử trùng lặp 
        # - Set không có thứ tự

+ tuple # - Là 1 giá trị , là 1 cấu trúc dữ liệu mà có thứ tự có thể chứa các phần tử trùng lặp và tạo bởi dấu ()
        # - Bản thân nó không thể thay đổi và các giá trị bên trong nó
"""

# Tuple
print("------Tuple-------")
tup1 = (1,2,3)
print(type(tup1))

tup2 = 1,2,3
print(type(tup2))

tup3 = 1,
print(type(tup3))

tup4 = (4,)
print(type(tup4))

print(tup1[-1])

# tup1[0] = 1000 # Error

# Cách để thêm giá trị vào tuple
tup1 += (4,5,6,7,1)
print(tup1)

print("------Set--------")

set1 = set()
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
# Không lặp lại nên trong set1 chỉ có 1 phần tử 10
print(set1)

# Có thể update bằng 1 cái list khác
set1.update([2, 3, 4, 5])
print(set1)
set1.remove(10)
print(set1)
set2 = set1.copy()
set1.clear()

print(set1)
print(set2 is set1)

set3 = {1,2,3,4}

# set3.add([12,3,4]) #List là 1 kiểu có thể thay đổi nhưng SET thì không, thêm được khi và chỉ khi những thứ đó là bất biến
set3.add("Kenny")
print(set3)
# SET không có thứ tự nên không thể truy cập bằng chỉ số
# print(set3[0]) # Wrong

# set.pop() Return a random value in list and remove it



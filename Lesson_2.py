user_name = "Kenny"
age = 20

# List: Lưu trữ nhiều dữ liệu => [ , , ... ]
# Chỉ số:  0  1   2   3
#         -4  -3  -2  -1
numbers = [1, 2, 3.5, 4]
print(type(numbers))
print(numbers)

print(numbers[0]) # Truy cập vào phần từ đầu tiên
print(numbers[3]) # Truy cập vào phần tử cuối cùng
print(numbers[-1]) 
print("--------------------")

print("-------Append-------")
numbers.append(1) # Thêm giá trị vào cuối và 1 chú ý cực kì QUAN TRỌNG là: f.append() nó chỉ thực hiện chứ không có giá trị Return
# (Wrong) a = numbers.append(100)
# print(a) => Kết quả: None (No values)
print(numbers) 

print("-------Remove-------")
numbers.remove(1) # Xóa đi giá trị được tìm thấy đầu tiên, chứ không xóa đi toàn bộ
print(numbers)

print("-------Pop-------")
last_value = numbers.pop() # Xóa đi giá trị cuối và RETURN giá trị vừa xóa => phải khởi tạo biến để hứng nó
print(last_value)
print(numbers)

print("-------Extend-------")
numbers.extend([1000, 100, 125]) # Mở rộng list ban đầu ( thêm list mới vào cuối )
print(numbers)

print("-------Change value in List-------")
numbers[0] = 24
print(numbers)

print("-------Count value the same in List-------")
count = numbers.count(100)
print(count)

print("-------Clear all value in List-------")
# numbers.clear()

print("-------Length of List-------")
length = len(numbers)
print(length)

print("-------Insert-------")
numbers.insert(0,100) # Thêm giá trị vào vị trí bất kì (trong TH kia là 0)

print("-------Index-------")
print(numbers)
index_of_3p5 = numbers.index(100) # Hàm f.index() chỉ tìm được vị trí của 1 GIÁ TRỊ duy nhất, nếu có tìm giá trị mà xuất hiện 2 lần trở lên trong list -> RETURN 0
print(index_of_3p5)

print("-------Reverse-------")
numbers.reverse() # Đảo ngược list và không có RETURN
print(numbers)

print("-------Del-------")
del numbers[1] # Xóa ở vị trí 1
# Sự khác nhau giữa del và remove thì del nó sẽ giải phóng cả bộ nhớ nữa còn remove thì không

friends = ["Jack", "John", "Kenny", "Henry"]
print(friends[0])
"""
+ list in list
+ copy list
+ list slicing

"""
print("---------------List in list--------------")
#                0           1             2
friends = [["Bob", 23], ["Jen", 34], ["Kenny", 56]]
print(friends[0][0])

print("----------------Copy list------------")
lst1 = [1 , 3, 2]
lst2 = lst1
# is: Toán tử dùng để kiểm tra địa chỉ (ID) -> True False
print(lst1 is lst2)
print(lst1 == lst2)

#Copy : Tất nhiên là giá trị của nó giống nhau còn địa chỉ của nó khác nhau
lst3 = [1, 3, 4]
lst4 = lst3.copy()

# is
# id: Lấy ra địa chỉ (giống pointer &)
print(id(lst3), id(lst4))
print(lst3 is lst4)
print(lst3 == lst4)

print("----------------List slicing------------")
#    0  1   2   3    4
a = [1, 3, 10, 100, 45]
new_lst = a[0:2:1] # [start:end:step] không lấy giá trị ở end, default step 1
print(new_lst)
print(new_lst is a)

# Chú ý QUAN TRỌNG ĐỐI hàm copy trong List

lst1 = [[1, [2, 3]], (4,5)]
lst2 = lst1[:] # Sử dụng lst1[:] hoặc lst1.copy() là như nhau

lst1[0][1].append(100)

print(lst2) # Kết quả: lst1 = [[1, [2, 3, 100], (4,5)] .
            # Lí do bởi vì line 106: khi sử dụng chỉ copy ngoặc vuông [] ngoài cùng, mặc dù lst1 và lst2 là 2 cái khác nhau, nên khi thay đổi LIST bên trong lst1 thì lst2 vẫn thay đổi

# Cách sửa : from copy (library) import in copy
from copy import deepcopy #deepcopy: copy sâu, hiểu như là copy toàn bộ
lst3 = [[3, [4, 5]], (1,2)]
lst4 = deepcopy(lst3)

lst3[0][1].append(100)

print(lst4)
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
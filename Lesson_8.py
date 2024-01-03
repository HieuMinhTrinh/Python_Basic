""" # Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách
# Cách 1
odd = even = 0
for i in range(1001):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"So le: {odd}")
print(f"So chan: {even}")
# Cách 2
lst_odd = [o for o in range(1001) if o % 2 != 0] # range() => class: 'range'
lst_even = [e for e in range(1001) if e % 2 == 0]

print(f"So le: {len(lst_odd)}")
print(f"So chan: {len(lst_even)}")
print(type(range(100)))

# Nhập vào 1 danh sách những số nguyên và hiển thị gấp đôi các số trong danh sách, sử dụng list
lst = map(int, input("Nhap 1 mang cac so nguyen: ").split())
new_lst = [val*2 for val in lst]
print(new_lst)
# Cho dict như sau:
import json
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29
}
# In ra ngoai tuoi lon nhat
max_age = 1
name = ""
for k,v in people.items():
    if v >= max_age:
        max_age = v
        name = k
print(f"Tuoi lon nhat:{name}-{max_age}")

# Tạo ra một dict mới dựa vào people với tuổi của mỗi người tăng gấp đôi
new_dict_people = {
    name: age*2
    for name, age in people.items()
}
print(new_dict_people)

# In ra enumerate các key trong people dict
print(list(enumerate(people)))

# Sử dung hàm dict để biến enumerate bên trên trở thành dict
new_people_1 = dict(enumerate(people))
print(json.dumps(new_people_1, indent=4))

# Sử dụng zip function để tạo 2 lists sau thành trở 1 dict
fruit = ["banana", "apple", "kiwi"]
amount = [12, 34, 90]

new_dict = dict(zip(fruit, amount))
print(json.dumps(new_dict , indent=4))
"""
"""
Python functions
"""
def my_func ():
    print("Hello World!")

def show_full_name(fname, lname):
    print(f"{fname} {lname}")

show_full_name("John","Doe") 

def add (x, y = 40):
    return x + y

print(add(y = 10, x = 100)) # Truyen theo ten chu khong theo vi tri

def func(lst = []): # CHÚ Ý: List hoặc Dict là có thể thay đổi nên phải TRÁNH 2 cái này làm tham số của Function               
    lst.append(2)   #        Tuple thì không thể thay đổi
    print(lst)

func()
func() # Kết quả: lst= [2,2]

#Local variable - Global variable
friends = ["Kenny", "Bob", "Jen"] # Global variable

def my_func():
    f = friends + ["Joe"] # Local variable 
    print(f)              # Trong python thì khi tên global variable == local variable thì sẽ xảy ra lỗi, cách fix, chỉ cần thay đổi tên biến của local variable là OK!

my_func()

add = (lambda x, y: x + y) # Hàm không có tên
print(add(1,2))

def greet(msg):
    print("Hello " + msg)
    return None

hello = greet
print(hello("Jen")) # In ra : Hello Jen bởi vì hello("Jen") trước màu tím 
                    #       : None      sau đó mới print() ngoài line 101

def func():
    pass # Dùng để tránh 1 hàm có phần thân khác trống bởi trong Python 1 hàm bắt buộc phần thân khác trống
         # Do nothing
# *args
def add (x, y, z, t):
    return x + y + z + t

print(add(1,2,3,4))

def add_1(*args): # CHÚ Ý: 1 dấu sao (*) : là tập hợp tất cả các đối số vị trí để tạo thành 1 cái tuple lưu bởi biến args: args = ()
    print(type(args)) # Type args: tuple    # 2 dấu sao (**): Là tập hợp tất cả các đối số có tên 
    return sum(args)

print(add_1(1,2,3,4))

lst = [4, 3, 2, 1]
print(*lst) # *lst là PHÁ cái list này ra tức là không có dấu ngoặc VUÔNG
#print(4, 3, 2, 1)

tup = (1,2,3,4)
print(*tup) # *tup PHÁ cái tuple này ra tức là không có dấu ()
#print(1,2,3,4)

lst_1 = [3, 10, 4, 5, 6, 7]
print(*lst_1[1:-1])

first, *mid, last = lst
print(first)
print(mid)
print(last)

def add(*lst, operation):
    return operation(lst)
print(add(1,2,3,4, operation=sum))

# Ví dụ khá hay : Đừng bao giờ nhân 1 list với 1 số
lst2 = [[]] * 3
lst2[1].append(2)
print(lst2) # Kết quả: [[2], [2], [2]]

lst3 = [[] for _ in range(3)]
lst3[1].appen(2)
print(lst3) # Kết quả: [[], [2], []]
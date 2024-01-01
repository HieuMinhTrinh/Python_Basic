"""

+ Advanced Set
+ Dictionary
+ sum, len, min, max, join

"""
set1 = {1 , 4, 3, 2}
set2 = {2, 3, 10, -10}

set3 = set1.intersection(set2) # Return a new set, và intersection set1 and set2
print(set3)

print(set1 & set2)

set4 = set1.difference(set2) # Return a new set, nằm trong set1 không nằm trong set2
print(set4)

print(set1 - set2)

set5 = set1.union(set2) # Lấy tất cả
print(set1 | set2)

set6 = set1.symmetric_difference(set2) # lấy tất cả nhưng trừ đi phần chung
print(set6)
print(set1 ^ set2)
print("------Dictionary------")
# Dictionary: key and value
import json

student = {

    "name": "Bob",
    "age" : 23,
    "grades": [45, 67, 90, 98, 99]
}
print(json.dumps(student, indent=4))

# value = student["name"]
# print(value)

value = student.get("id", "SV001")
print(value)

student["id"] = "SV001"
student["name"] = "Jack"
print(student)

student.update(id = "SV002", gender="male")
print(json.dumps(student, indent = 4))

info = {
    'id': "SV003",
    'gender': 'female'
}
student.update(info)
print(json.dumps(student, indent = 4))

# remove
values = student.pop('name') # Return value of key
print(json.dumps(student, indent=4))
print(values)

del student["id"]
print(json.dumps(student, indent=4))

tup = student.popitem() # Xóa đi cái cuối cùng trong Dict và trả ra tup của cái đó
print(tup)
print(json.dumps(student, indent=4))

#Lấy ra tất cả các key in dictionary và biến nó trở thành 1 List
keys = list(student)
print(keys)
#Lấy ra tất cả các giá trị in dictionary và biến nó trở thành 1 List
values = list(student.values())
print(values)

items = list(student.items())
print(items)
#clear
student.clear()
print(student)

print("--------------------")

lst = [1, 2, 3, 4]
total = sum(lst)
print(total)

lst = ['a', 'b', 'c', 'f']
print(len(lst))

# min , max => Bắt buộc phải có các giá trị
#              Chỉ sử dụng trên số (int, float, ...)
# join
lst = [4,2,3,1]
s = ' - '.join(map(str, lst)) # Hàm map convert từng giá trị ở lst thành str
print(s)
# Bài tập
"""
Yêu cầu:
a, Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
b, Thay đổi giá trị của key: release_year từ 1973 thành 1971
c, Xóa phần tử với key là track_list
d, Thêm một key mới là amount = 2000 bằng 2 cách
e. Làm trống dict: album_info
"""
import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": "1971",
    "track_list": [
            "Speak to Me",
            "Breathe",
            "On the Run",
            "Time",
            "The Great Gig in the Sky",
            "Money",
            "Us and Them",
            "Any Colour You Like",
            "Brain Damage",
            "Eclipse",
    ]
}
# a, Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
# Cách 1:
print(f"C1.Album: {album_info['album_name']} and Release: {album_info['release_year']}")
# Cách 2:
print(f"C2.Album: {album_info.get('album_name')} and Release: {album_info.get('release_year')}")
# b, Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info['release_year'] = 1973
print(json.dumps(album_info, indent= 4))

# c, Xóa phần tử với key là track_list
# del album_info['track_list']
# print(json.dumps(album_info, indent= 4))
value = album_info.pop("track_list")
print(value) # value là 1 List chứa những key vừa pop
print(json.dumps(album_info, indent= 4))
# d, Thêm một key mới là amount = 2000 bằng 2 cách
# album_info['amount'] = 2000
# print(json.dumps(album_info, indent= 4))
update_key = {
    "amount": 2000
}
album_info.update(update_key)
print(json.dumps(album_info, indent= 4))

#e. Làm trống dict: album_info 
album_info.clear()
print(json.dumps(album_info, indent= 4))

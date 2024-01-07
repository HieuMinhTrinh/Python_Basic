""" 
lst = [4,100,5,6]

for value in lst:
    print(value) """
# Với tuple cũng vậy

d = {
    "a":1,
    "b":2,
    "c":3
}
for key in d:
    print(key)
for value in d.values():
    print(value)

for item in d.items():
    key, value = item
    print(key)
    print(value)
    print('-'*20)
    
# List comprehensions => Luôn tạo ra cái mới
a = [2, 4, 6, 8]

# new_a = [4,8,12,16]
""" new_a =[]
for x in a:
    val = x * 2
    new_a.append(val) """
#List comprehensions
new_lst = [val*2 for val in a] 
print(new_lst)

# Set comprehensions => Luôn tạo ra cái mới
set_a = {'a', 'b', 'c'}
new_set = {s.upper() for s in set_a}
print(new_set)

# dict comprehensions => Luôn tạo ra cái mới
new_d = {
    k: v*2
    for k, v in d.items()
}
print(new_d)
print(d)

"""
+, zip
+, enumerate

"""
lst1 = ['a', 'b', 'c', 'd']
lst2 = (1, 2, 3, 4, 5)
lst3 = ['a1', 'b1', 'c1', 'd1']
print(list(zip(lst1, lst2, lst3)))
#       1    2    3
lst = ["a", "b", "c"]
print(list(enumerate(lst, start = 1))) # List tup

lst4 = ('a', 'b', 'c')
lst5 = (1,2,3)

print(dict(zip(lst4, lst5)))

lst6 = [1, 2, 3, 4]
new_lst6 = [ val**3 for val in lst6] # List comprehensions
print(new_lst6)


numbers = [100, 34, 56, 78, 89, -46, 33, 77]

new_list = [ value for value in numbers if value % 2 != 0]
print(new_list)
print(sum(new_list))

new_list2 = [value*2 if value % 2 == 0 else value*3 for value in numbers]

# zip
# enumerate => (), (), ()
lst7 = [1,2,3,4]
# Yêu cầu: {i} - {value}
print(list(enumerate(lst7)))
for item in enumerate(lst7, start = 1): 
    idx,v = item
    print(f"{idx} - {v}")

# In ra index của list7
for idx in range(len(lst7)):
    if idx % 2 != 0:
        print(idx, lst7[idx])


for k, v in enumerate(lst7):
    if k % 2 != 0:
        print(k , v)

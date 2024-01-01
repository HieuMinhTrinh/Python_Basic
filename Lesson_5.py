"""
if - else - elif
"""
if 1 > 0:
    print("1 > 0")
else:
    print("1 <= 0")

# n = int(input("n = "))

""" if n > 0:
    print("So duong")
elif n < 0:
    print("So am")
else:
    print("So 0")
"""
    # Shift + Alt + A 
#print("n chia het cho 3" if n % 3 == 0 else "n khong chia het cho 3")

a ,b = map(int, input().split()) #split() bỏ khoảng trắng

print(a if a < b else b)

#eval
lst = list(map(eval, input().split())) # Có thể nhập cả số nguyên lẫn số thực trên cùng 1 hàng
a = 2
print(type(eval("a+22"))) #int
print(lst)

lst = [ 1, 2, 3, 4 ]
# 1 2 3 4
print(*lst) # *: Phá vỡ cái lst này ra, phá ngoặc vuông
# print(*lst, sep = " % ")

x = 2.34567
print(format(x, ".2f")) # Làm tròn tới 2 chữ sỗ thập phân sau dấu phẩy

#round
x = 2.456
print(round(x, 2)) 

# sorted
lst = [4,3,2,10]
new_lst = sorted(lst, reverse=True)
print(new_lst)
# ord - chr
char = 'a'
print("ASCII Code: ", ord(char))

ascii_code = 65
print(chr(ascii_code))

s = "abcd"
print(list(s)) # ['a','b','c','d']

lst = list(map(eval, input().split()))



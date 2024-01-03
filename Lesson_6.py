"""
+, For, while, từ khóa break, continue, mệnh đề else
+, Break: Thoát hoàn toàn ra khỏi vòng lặp chứa nó
+, Continue: Bỏ qua các câu lệnh bên dưới nó và chuyển sang một lần lặp mới

"""
for _ in range(5):
    print("Hello World!")

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end = ' ')

s = input(" > ")

while s != 'q':
    print("hello")
    s = input()
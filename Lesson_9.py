# Định nghĩa menu hiển thị gợi ú người dùng nhập tùy chọn (option)
USER_MENU = """
a - Add new film
b - Print all film
c - Find film
d - Delete film with name
u - Update film
q - Exit
Your option: """
# Định nghĩa cấu trúc dữ liệu lưu trữ các bộ phim
# List[dict]: Mỗi bộ phim là 1 dictionary nằm trong List
movies = []

#Kiêm tra các bộ phim duy nhất
prevs = set()

# Định nghĩa các hàm xử lý
# Add a new film
def add_movies():
    # Nhập thông tin bộ phim
    name             = input("Enter the movie name\t: ")
    while name in prevs:
        print("Movie names are duplicated\t")
        name         = input("Enter the movie name\t: ")
        
    director         = input("Enter the movie director\t: ")
    release_year     = input("Enter release of the movie\t: ")
    # Tạo ra bộ phim
    movie = {
        'name'          : name,
        'director'      : director,
        'release_year'  : release_year
    }

    # Thêm vào danh sách
    movies.append(movie)
    prevs.add(name)

# Hiển thị thông tin bộ phim
def show_movie(idx):
    movie_name = movies[idx]['name']
    movie_director = movies[idx]['director']
    movie_release_year = movies[idx]['release_year']

    print(f"Name of movie\t: {movie_name}")
    print(f"Director of movie\t: {movie_director}")
    print(f"Release year of movie\t: {movie_release_year}")

# Hiển thị thông tin bộ phim
def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start = 0):
            print("INFORMATION OF MOVIE", idx+1)
            show_movie(idx)
    else:
        print("List is empty")

#Tìm kiếm phim theo tên
def search_movies():
    if movies:
        movie_name = input("Name of movie you wants to search: ")
        for idx, movie in enumerate(movies, start = 0):
            if movie_name == movie['name']:
                print("INFORMATION OF MOVIE", idx+1)
                show_movie(idx)
                break
            elif idx == len(movies)-1:
                print("Not found!")
    else:
        print("List is empty")


# Xóa phim theo tên
def remove_movies():
    if movies:
        movie_name_del = input("Name of movie you wants to delete: ")
        for idx, movie in enumerate(movies, start = 0):
            if movie_name_del == movie['name']:
                del(movies[idx])
                print("Completed delete!")
                break
            else:
                print("Not found!")
    else:
        print("List is empty")

# Cập nhập thông tin phim
def update_inf_movies():
    if movies:
        update_name_film = input("Enter the movie name\t: ")
        
        founds = [
            idx 
            for idx, movie in enumerate(movies)
            if movie['name'] == update_name_film
        ]

        if founds:
            position                         = founds[0]
            movies[position]['director']     = input("Enter the movie director\t: ")
            movies[position]['release_year'] = input("Enter release of the movie\t: ")
            print("Completed update!")
        else:
            print("Not found", update_name_film)
    else:
        print("List is empty")

# Nhập sự lựa chọn của users:
user_choice = input(USER_MENU)

# Định nghĩa 1 dict dùng để lưu chữ các option
operations = {
    'a': add_movies,
    'b': show_movies,
    'c': search_movies,
    'd': remove_movies,
    'u': update_inf_movies
}

# Chọn đến khi thoát
while user_choice != 'q':
    if user_choice in operations:
        # Lấy ra giá trị của key: user_choice
        operation = operations[user_choice]
        operation() # Gọi hàm tương ứng với tùy chọn
    else:
        print("Invalid!")
    
    user_choice = input(USER_MENU)



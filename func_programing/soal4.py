# decorator
def make_bold(func):
    def wrapper():
        # menggunakan fungsi ansi escape code 
        return f"\033[1m{func()}\033[0m"  # 1m untuk bold
    return wrapper

def make_italic(func):
    def wrapper():
        return f"\033[3m{func()}\033[0m"  # 3m untuk italic
    return wrapper

def make_underline(func):
    def wrapper():
        return f"\033[4m{func()}\033[0m"  # 4m untuk underline
    return wrapper

# Fungsi hello dengan tiga decorator
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

# Pemanggilan fungsi
print(hello())

import time

# 1

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print("У вас нет доступа")
    return wrapper

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


admin = User("Ardager", "admin")

user = User("Bek", "user")

@is_admin
def delete_video(user):
    print("Видео удалено")


delete_video(user)


# 2

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {round(end - start, 2)} секунд")
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")



download_video()

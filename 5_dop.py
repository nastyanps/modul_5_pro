from time import sleep


class User:
    def __init__(self, nickname, password, age=0):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


    def __str__(self):
        return f'Название: {self.title}'




class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == password:
                self.current_user = User(nickname, password)
                break


    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.current_user = user
        else:
            print(f'Пользователь {user.nickname} уже существует')


    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if video not in self.videos:
                self.videos.append(i)

    def get_videos(self, request):
        result = []
        for i in self.videos:
            if request.lower() in i.title.lower():
                result.append(i.title)
        return result

    def watch_video(self, film_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
        else:
            for i in self.videos:
                if film_name.lower() in str(i.title).lower():
                    for j in range(i.time_now, i.duration + 1):
                        print(j, end=' ')
                        sleep(0.1)
                    print('Конец видео')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

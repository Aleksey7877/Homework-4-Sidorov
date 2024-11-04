import requests
import json

# задача 1


def posts_of_5():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        data = response.json()  # Получаем данные в формате JSON
        for i in range(0, 5):
            print(
                f"Пост №{i+1}. Заголовок: {data[i]['title']}: \nТекст: {data[i]['body']} \n")
    else:
        print(f'Ошибка: {response.status_code}')

# posts_of_5()


# задача 2
def city_weather(city_name: str) -> None:
    city_coordinates = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={
                                    city_name}&limit=5&appid=a31bf60829b8edb1b7d099432ef301f7x')
    if city_coordinates.status_code == 200:
        information_of_city = city_coordinates.json()
        lat = information_of_city[0]['lat']
        lon = information_of_city[0]['lon']
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={
            lat}&lon={lon}&appid=a31bf60829b8edb1b7d099432ef301f7')
        weather_of_city = weather.json()
        print(f"Погода в городе {city_name} : Температура: {int(weather_of_city['main']['temp']) - 273} градусов, ощущается как {int(weather_of_city['main']['feels_like']) - 273} градусов. Колебания температуры от {
            int(weather_of_city['main']['temp_min']) - 273} до {int(weather_of_city['main']['temp_max']) - 273} градусов, давление: {float(weather_of_city['main']['pressure'])/10} кПа, влажность: {weather_of_city['main']['humidity']} %, дальность обзора: {weather_of_city['visibility']} метров, ветер: {weather_of_city['wind']['speed']} м/с")
    else:
        print(f'Ошибка: {city_coordinates.status_code}')

# city_weather(input(print("Введите название города: ")).capitalize())

# задача 3


def post_to_place():
    title = input(print("Введите заголовок поста."))
    body = input(print("Введите текст поста."))
    user_post = requests.post('https://jsonplaceholder.typicode.com/posts', {
        'method': 'POST',
        'body': json.dumps({
            'title': title,
            'body': body,
            'userid': 1,
        }),
        'headers': {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    if user_post.status_code == 201:
        print(f"Ваш пост под названием: {json.loads(user_post.json()['body'])[
              'title']}, содержимое поста: {json.loads(user_post.json()['body'])['body']}")
    else:
        print(f'Ошибка: {user_post.status_code}')

# post_to_place()

# задача 4


def post_to_place_2():
    title = input(print("Введите заголовок поста."))
    body = input(print("Введите текст поста."))
    user_post = requests.post('https://jsonplaceholder.typicode.com/posts', {
        'method': 'POST',
        'body': json.dumps({
            'title': title,
            'body': body,
            'userid': 1,
        }),
        'headers': {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    if user_post.status_code == 201:
        print(f"Ваш пост под названием: {json.loads(user_post.json()['body'])[
              'title']}, содержимое поста: {json.loads(user_post.json()['body'])['body']}")
    elif user_post.status_code == 400:
        print(f'Ошибка: {user_post.status_code}. Неверны данные.')
    elif user_post.status_code == 404:
        print(f'Ошибка: {user_post.status_code}. Неверно указана ссылка.')
    else:
        print(f'Ошибка: {user_post.status_code}')

# post_to_place_2()

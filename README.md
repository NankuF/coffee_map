# Создание карты с ближайшими кафе вокруг вас. (Москва)

## Запуск проекта:

1. Скачайте проект:<br>
```commandline
git clone https://github.com/NankuF/coffee_map.git
```
2. Создайте виртуальное окружение:<br>
```commandline
python -m venv venv
```
3. Установите зависимости:<br> 
```commandline
pip install -r requirements.txt
```
4. Создайте файл `.env` и добавьте в него ключ апи полученный в Яндексе
   (https://developer.tech.yandex.ru/services/):
```commandline
YA_APIKEY = 'ваш ключ апи к сервису Яндекса'
```
5. Запустите код в консоли:<br>
```commandline
python main.py
```
6. Перейдите в браузере по адресу:<br>
```commandline
http://127.0.0.1:5000
```
7. Выберите подходящее кафе:<br>
![img.png](img.png)
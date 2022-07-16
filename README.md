# Создание карты с ближайшими кафе вокруг вас. (Москва)

## Запуск проекта:

1. Скачайте проект:<br>
```commandline
git clone https://github.com/NankuF/coffee_map.git
```
2. Перейдите в директорию:
```commandline
cd coffee_map
```
3. Создайте виртуальное окружение:<br>
```commandline
python -m venv venv
```
4. Активируйте виртуальное окружение:<br>
Windows<br>
```commandline
. .\venv\Scripts\activate
```
Linux<br>
```commandline
. ./venv/bin/activate
```
5. Установите зависимости:<br> 

```commandline
pip install -r requirements.txt
```
6. Создайте файл `.env` и добавьте в него ключ апи полученный в Яндексе
   (https://developer.tech.yandex.ru/services/):
```commandline
YA_APIKEY = 'ваш ключ апи к сервису Яндекса'
```
7. Запустите код в консоли:<br>
```commandline
python main.py
```
8. Перейдите в браузере по адресу:<br>
```commandline
http://127.0.0.1:5000
```
9. Выберите подходящее кафе:<br>
![img.png](img.png)

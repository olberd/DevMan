# Обрезка ссылок с помощью Битли

Программа для генерации коротких ссылок с помощью сервиса [bitly.com](https://bitly.com/), а также для проверки количества кликов по уже созданным ссылкам.
## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

Для работы скрипта нужна регистрация на сервисе [bitly.com](https://bitly.com/). Регистрируйтесь на Bitly через e-mail вместо социальных сетей. 
После регистрации Вы получите `GENERIC ACCESS TOKEN` — нужный тип токена вида `17c09e20ad155405123ac1972fecf00231da7`.
После получения уникального токена в папке со скриптом создайте текстовый файл .env, в который запишите следующее:

`TOKEN_BITLY==ВАШ_ТОКЕН`

Для запуска в консоли:
```
$ python main.py http://ссылка_для_сокращения 
```
и/или
```
bit.ly/сокращенная_ссылка 
```
количество ссылок для сокращения или проверки на клики не ограничено.

Пример использования:


`python.exe main.py https://mail.ru/`

или с сокращенной ссылкой

`python.exe main.py https://bit.ly/3GwsETo`


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
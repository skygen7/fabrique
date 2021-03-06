Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Run:
1. Install packages: $ pip install -r requirements.txt
2. Migrate: $ python manage.py migrate
3. Admin: $ python manage.py createsuperuser
4. Run: $ python manage.py runserver

Нюансы:
Выбор типа вопроса следующий (задавать эти название в поле type):
one correct: ответ с выбором одного варианта
multiple choice: ответ с выбором нескольких вариантов
text: ответ текстом
Ответы и варианты заполнять через запятую с пробелом между словами

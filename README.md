# Проект API YaMDb

## Описание

**YaMDb** - это проект, который собирает отзывы пользователей на различные произведения, такие как книги, фильмы и музыка. Сам проект не хранит произведения; это платформа для пользователей, где они могут делиться своими мнениями и оценками.

## Технологии

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Авторы

### [Кирилл Мансуров](https://github.com/Kirill374mansurov)</br>
Разрабатывал модели, view и эндпойнты для:
- произведений, 
- категорий, 
- жанров;</br> 
Реализация импорта данных из csv файлов. 
    

### [Евгений Олейников](https://github.com/olejnikoves2)</br>
Разрабатывал модели, view и эндпойнты для:
- отзывов, 
- комментариев, 
- рейтингов произведений.
    

### [Александр Мальцев](https://github.com/clifforc)</br>
Разрабатывал часть, касающуюся управления пользователями:
- систему регистрации и аутентификации, 
- права доступа, 
- работу с токеном, 
- систему подтверждения через e-mail.
  

## Функциональность

- Произведения разделены на категории (например, "Книги", "Фильмы", "Музыка")
- Произведениям можно присваивать жанры (например, "Сказка", "Рок", "Артхаус")
- Пользователи могут оставлять текстовые отзывы и оценивать произведения по шкале от 1 до 10
- На отзывы можно оставлять комментарии
- Система аутентификации и авторизации пользователей

## Роли пользователей

- **Аноним** - Может просматривать описания произведений, читать отзывы и комментарии
- **Аутентифицированный пользователь (`user`)** - Может читать всё, публиковать отзывы, ставить оценки произведениям, комментировать отзывы, а также редактировать свои отзывы, комментарии и оценки
- **Модератор (`moderator`)** - Те же права, что и у аутентифицированного пользователя, плюс возможность удалять и редактировать любые отзывы и комментарии
- **Администратор (`admin`)** - Полные права на управление всем контентом, может создавать и удалять произведения, категории и жанры, а также назначать роли пользователям

## Ресурсы API

- `/auth/`: Аутентификация
- `/users/`: Управление пользователями
- `/titles/`: Произведения (фильмы, книги, песни)
- `/categories/`: Категории произведений
- `/genres/`: Жанры произведений
- `/reviews/`: Отзывы на произведения
- `/comments/`: Комментарии к отзывам

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Kirill374mansurov/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv .venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Импортировать данные:

```
python manage.py run_import
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов к API:

### Регистрация нового пользователя:

Права доступа: **Доступно без токена**

```http request
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "^w\\Z"
}
```

### Получение JWT-токена:

Права доступа: **Доступно без токена**

```http request
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
"username": "^w\\Z",
"confirmation_code": "string"
}
```

### Получение списка всех категорий:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/categories/
```

### Добавление новой категории:

Права доступа: **Администратор**

```http request
POST http://127.0.0.1:8000/api/v1/categories/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "slug": "^-$"
}
```

### Удаление категории:

Права доступа: **Администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/
Authorization: Bearer <your_access_token>
```

### Получение списка всех жанров:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/genres/
```

### Добавление жанра:

Права доступа: **Администратор**

```http request
POST http://127.0.0.1:8000/api/v1/genres/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "slug": "^-$"
}
```

### Удаление жанра:

Права доступа: **Администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/genres/{slug}/
Authorization: Bearer <your_access_token>
```

### Получение списка всех произведений:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/
```

### Добавление произведения:

Права доступа: **Администратор**

```http request
POST http://127.0.0.1:8000/api/v1/titles/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

### Частичное обновление информации о произведении:

Права доступа: **Администратор**

```http request
PATCH http://127.0.0.1:8000/api/v1/titles/{titles_id}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

### Удаление произведения:

Права доступа: **Администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{titles_id}/
Authorization: Bearer <your_access_token>
```

### Получение списка всех отзывов:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```


### Получение информации о произведении:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```

### Добавление нового отзыва:

Права доступа: **Аутентифицированные пользователи**

```http request
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string",
  "score": 1
}
```

### Получение отзыва по id:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```

### Частичное обновление отзыва по id:

Права доступа: **Автор отзыва, модератор или администратор**

```http request
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string",
  "score": 1
}
```

### Удаление отзыва по id:

Права доступа: **Автор отзыва, модератор или администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
Authorization: Bearer <your_access_token>
```

### Получение списка всех комментариев к отзыву:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

### Добавление комментария к отзыву:

Права доступа: **Аутентифицированные пользователи**

```http request
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string"
}
```

### Получение комментария к отзыву:

Права доступа: **Доступно без токена**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

### Частичное обновление комментария к отзыву:

Права доступа: **Автор комментария, модератор или администратор**

```http request
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string"
}
```

### Удаление комментария к отзыву:

Права доступа: **Автор комментария, модератор или администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Authorization: Bearer <your_access_token>
```

### Получение списка всех пользователей:

Права доступа: **Администратор**

```http request
GET http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer <your_access_token>
```

### Добавление пользователя:

Права доступа: **Администратор**

```http request
POST http://127.0.0.1:8000/api/v1/users/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "username": "^w\\Z",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

### Получение пользователя по username:

Права доступа: **Администратор**

```http request
GET http://127.0.0.1:8000/api/v1/users/{username}/
Authorization: Bearer <your_access_token>
```

### Изменение данных пользователя по username:

Права доступа: **Администратор**

```http request
PATCH http://127.0.0.1:8000/api/v1/users/{username}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "username": "^w\\Z",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

### Удаление пользователя по username:

Права доступа: **Администратор**

```http request
DELETE http://127.0.0.1:8000/api/v1/users/{username}/
Authorization: Bearer <your_access_token>
```

### Получение данных своей учетной записи:

Права доступа: **Любой авторизованный пользователь**

```http request
http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer <your_access_token>
```

### Изменение данных своей учетной записи:

Права доступа: **Любой авторизованный пользователь**

```http request
PATCH http://127.0.0.1:8000/api/v1/users/me/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "username": "^w\\Z",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
```
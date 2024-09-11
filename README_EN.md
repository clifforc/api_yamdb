# YaMDb API Project

## Description

**YaMDb** is a project that collects user reviews on various works such as books, movies, and music. The project itself does not store the works; it's a platform for users to share their opinions and ratings.

## Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Authors

### [Alexander Maltsev](https://github.com/clifforc)
Developed the user management part:
- Registration and authentication system
- Access rights
- Token handling
- Email confirmation system

### [Kirill Mansurov](https://github.com/Kirill374mansurov)
Developed models, views, and endpoints for:
- Works
- Categories
- Genres
Implementation of data import from CSV files.

### [Evgeny Oleynikov](https://github.com/olejnikoves2)
Developed models, views, and endpoints for:
- Reviews
- Comments
- Work ratings

## Functionality

- Works are divided into categories (e.g., "Books", "Movies", "Music")
- Works can be assigned genres (e.g., "Fairy Tale", "Rock", "Arthouse")
- Users can leave text reviews and rate works on a scale from 1 to 10
- Comments can be left on reviews
- User authentication and authorization system

## User Roles

- **Anonymous** - Can view descriptions of works, read reviews and comments
- **Authenticated user (`user`)** - Can read everything, publish reviews, rate works, comment on reviews, and edit their own reviews, comments, and ratings
- **Moderator (`moderator`)** - Same rights as an authenticated user, plus the ability to delete and edit any reviews and comments
- **Administrator (`admin`)** - Full rights to manage all content, can create and delete works, categories, and genres, as well as assign roles to users

## API Resources

- `/auth/`: Authentication
- `/users/`: User management
- `/titles/`: Works (movies, books, songs)
- `/categories/`: Work categories
- `/genres/`: Work genres
- `/reviews/`: Reviews of works
- `/comments/`: Comments on reviews

## How to run the project:

Clone the repository and navigate to it in the command line:

```
git clone https://github.com/clifforc/api_yamdb.git
```

```
cd api_yamdb
```

Create and activate a virtual environment:

```
python3 -m venv .venv
```

* For Linux/macOS

    ```
    source env/bin/activate
    ```

* For Windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

Perform migrations:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Import data:

```
python3 manage.py run_import
```

Run the project:

```
python3 manage.py runserver
```

## Examples of API requests:

### Register a new user:

Access rights: **Available without token**

```http request
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "^w\\Z"
}
```

### Obtain JWT token:

Access rights: **Available without token**

```http request
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
"username": "^w\\Z",
"confirmation_code": "string"
}
```

### Get list of all categories:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/categories/
```

### Add a new category:

Access rights: **Administrator**

```http request
POST http://127.0.0.1:8000/api/v1/categories/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "slug": "^-$"
}
```

### Delete a category:

Access rights: **Administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/
Authorization: Bearer <your_access_token>
```

### Get list of all genres:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/genres/
```

### Add a genre:

Access rights: **Administrator**

```http request
POST http://127.0.0.1:8000/api/v1/genres/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "name": "string",
  "slug": "^-$"
}
```

### Delete a genre:

Access rights: **Administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/genres/{slug}/
Authorization: Bearer <your_access_token>
```

### Get list of all works:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/
```

### Add a work:

Access rights: **Administrator**

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

### Partial update of work information:

Access rights: **Administrator**

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

### Delete a work:

Access rights: **Administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{titles_id}/
Authorization: Bearer <your_access_token>
```

### Get list of all reviews:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```

### Get information about a work:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```

### Add a new review:

Access rights: **Authenticated users**

```http request
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string",
  "score": 1
}
```

### Get a review by id:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```

### Partial update of a review by id:

Access rights: **Review author, moderator or administrator**

```http request
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string",
  "score": 1
}
```

### Delete a review by id:

Access rights: **Review author, moderator or administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
Authorization: Bearer <your_access_token>
```

### Get list of all comments to a review:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

### Add a comment to a review:

Access rights: **Authenticated users**

```http request
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string"
}
```

### Get a comment to a review:

Access rights: **Available without token**

```http request
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

### Partial update of a comment to a review:

Access rights: **Comment author, moderator or administrator**

```http request
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "string"
}
```

### Delete a comment to a review:

Access rights: **Comment author, moderator or administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Authorization: Bearer <your_access_token>
```

### Get list of all users:

Access rights: **Administrator**

```http request
GET http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer <your_access_token>
```

### Add a user:

Access rights: **Administrator**

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

### Get a user by username:

Access rights: **Administrator**

```http request
GET http://127.0.0.1:8000/api/v1/users/{username}/
Authorization: Bearer <your_access_token>
```

### Change user data by username:

Access rights: **Administrator**

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

### Delete a user by username:

Access rights: **Administrator**

```http request
DELETE http://127.0.0.1:8000/api/v1/users/{username}/
Authorization: Bearer <your_access_token>
```

### Get data of your own account:

Access rights: **Any authorized user**

```http request
GET http://127.0.0.1:8000/api/v1/users/me/
Authorization: Bearer <your_access_token>
```

### Change data of your own account:

Access rights: **Any authorized user**

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

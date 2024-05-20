# Yatube api
### Описание проекта:

Проект предоставляет backand api для проекта Yatube.
Api позволяет создавать и читать посты, оставлять комментарии
и подписываться на других пользователей.
Доступ к чтению комментариев и постов доступен анонимным пользователям.

### Используемые библиотеки:

Django 3.2.16,
pytest 6.2.4,
pytest-pythonpath 0.7.3,
pytest-django 4.4.0,
djangorestframework 3.12.4,
djangorestframework-simplejwt 4.7.2,
Pillow 9.3.0,
PyJWT 2.1.0,
requests 2.26.0

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Vlad-RND/yatube_api.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

Получение публикаций:

```
/api/v1/posts/
```

Получение комментариев:

```
/api/v1/posts/{post_id}/comments/
```

Список сообществ:

```
/api/v1/groups/
```

Подписки
Возвращает все подписки пользователя, сделавшего запрос.
Анонимные запросы запрещены.

```
/api/v1/follow/
```

Получить JWT-токен

```
/api/v1/jwt/create/
```

Автор - Vlad-RND,
GIT - https://github.com/Vlad-RND

# api_final
api final

### Описание проекта:

Проект предоставляет backand api для проекта Yatube.
Api позволяет регестрироваться, создавать и читать посты, оставлять комментарии
и подписываться на других пользователей.
Доступ к чтению комментариев и постов доступен анонимным пользователям.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Vlad-RND/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
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

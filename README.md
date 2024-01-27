# Анонимный чат

Краткое описание вашего проекта: что он делает, зачем он нужен, и т.д.

## Модели

Проект включает следующие модели данных:

### User

- `id` (Integer): Уникальный идентификатор пользователя.
- `username` (String): Имя пользователя.
- `password_hash` (String): Хеш пароля пользователя.

### Message

- `id` (Integer): Уникальный идентификатор сообщения.
- `content` (String): Текст сообщения.
- `sender_id` (Integer): Идентификатор пользователя, отправляющего сообщение.
- `receiver_id` (Integer): Идентификатор пользователя, получающего сообщение.

## API Endpoints

### Регистрация Пользователя

`POST /register`

Принимает JSON со следующими полями:
- `username`: Имя пользователя.
- `password`: Пароль пользователя.

### Получение Списка Пользователей

`GET /get_users`

Возвращает список всех пользователей.

### Отправка Сообщения

`POST /send_message`

Отправляет сообщение от одного пользователя другому. Принимает JSON со следующими полями:
- `content`: Текст сообщения.
- `sender_id`: ID пользователя, отправляющего сообщение.
- `receiver_id`: ID пользователя, получающего сообщение.

### Получение Всех Сообщений

`GET /get_messages`

Возвращает список всех сообщений. Каждое сообщение содержит:
- `id`: Уникальный идентификатор сообщения.
- `content`: Текст сообщения.
- `sender_id`: ID пользователя, отправившего сообщение.
- `receiver_id`: ID пользователя, получившего сообщение.

### Получение Сообщений (Тестовое)

`GET /receive_message`

Возвращает пример сообщения.

## Установка и Запуск

### Установка Зависимостей

Убедитесь, что у вас установлены все необходимые зависимости:

pip install -r requirements.txt

### Управление Миграциями

#### Инициализация Миграций

##### Выполнять в папке сервера

flask db init 


#### Создание Миграции

flask db migrate -m "Initial migration."


#### Применение Миграций

flask db upgrade


#### Откат Миграций

flask db downgrade


### Запуск Сервера

flask run

#### или в папке проекта

python .\server\app.py

## Авторы

Назаренко Глеб Максимович
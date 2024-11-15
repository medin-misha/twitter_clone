## не жалкий клон твиттера
Корпоративный клон твиттера с отсутствующей регистрацией. Вот как то так.
## как запустить? 
Для начала нужно запустить postgres
```commandline
docker-compose up --build
```
все все настройки postgres лежат в docker-compose.yml под дерективой `enviroment`
```yml
   # (настройки по умолчанию)
    environment:
      POSTGRES_USER: postgres_user
      POSTGRES_PASSWORD: postgres_password
      POSTGRES_DB: postgres_db
      PGDATA: /var/lib/postgresql/data/pgdata
```
Далее нужно запустить миграции командой
```commandline
alembic upgrade head
```
и запустить само приложение
```commandline
uvicorn "main:app" --reload
```
Готово.
## техническая документация
### main.py
В main.py содержиться код для запуска и подключения роутеров которые лежат
в папке handlers.

Роутеры именуются (так как их видно в main.py) в `__init__.py` по принцыпу 
`<name>_router`. 

### handlers
В папке handlers лежат функции обработки а так же в отдельной папке вынесены функции для общего использования в рамках обработчиков. 

Папка для функций общего использования называеться utils/ в ней пока что есть 2 файла
- responses.py папка в которой лежат функции ok_response и error_response.
- db_actions.py папка в которой лежат функции для общего взаемодействия со всеми моделей для базы данных

#### Какие функции за что отвечают
- responses.ok_response - Функция которая принимает данные ответа сервера (аргумент resp) и адаптирует данные под понимание фронтенда (по факту просто добавляет к ответу { "result": true })
- response.error_response - Функция которая возвращает ошибку которую понимает фронтенд (принимает аргументы msg - сообщение об ошибке и err_type который по факту являеться status кодом ошибки)
- db_actions.create - Функция которая должна по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД), и данных (data - словарь с данными для модели) создать запись в базе данных.
- db_actions.remove - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) и id (id записи в БД) удалять запись
- db_actions.get_by_id - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) и id (id записи в БД) отдаёт запись или None
- db_actions.get_list - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) возвращает все записи таблицы
### core
В папке core находиться файлы которые необходимы для работы проекта и работы с базой данных
- config.py - файл конфигурации
- database.py - файл работающий с базой данных
- models/ - директория с моделями для базы данных

#### Какие классы за что отвечают?
- config.Settings - класс конфигурации проекта пока что содержит 2 поля db_url - url к базе данных, image_saver_url - url к сервису который будет хранить и выдавать изображения для твитов.
- config.settings - Переменная с экземпляром класса Settings для более удобного импорта
- database.DBSettings - Класс который отвечает за взаемодействие с бд (создание движка (в __init__()) и выдачу сессий (в session()))
- database.db_settings - переменная с экземпляром класса DBSettings для более удобного импорта
- models.base.Base - Класс базовой модели базы данных от которого наследуются другие классы-модели. По умолчанию имеет поле id которое являеться первичным ключом.
- models.user/tweet/image - файлы с моделями базы данных
- models.table_communication - файл с промежуточными таблицами для моделей.

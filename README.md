# Название проекта
Проект "Online_Tech_Store"
Веб-приложение с API-интерфейсом и админ-панелью.
База данных, с использованием миграции Django.

## Содержание
В проекте созданы следующие приложения:
- users
- e_shop
- config

## Технологии

## Использование


## Разработка
- создан .gitignore 
- загружены зависимости и линтеры
- Создан проект и подключен DRF
- создана бд PostgreSQL для хранения данных
- создана админ-панель
- подготовлена команда для создания суперюзера (csu)
- созданы модели для e_shop (Supplier, Product, ProductSupplierRelation) и users
- созданы сериалайзеры
- прописаны представления через ViewSet
- прописаны urls для всех приложений
- в админ панели реализованы:
-- ссылка на «Поставщика»;
-- фильтр по названию города;
-- admin action, очищающий задолженность перед поставщиком у выбранных объектов
- настроено использование JWT-авторизации
- настроена авторизация по email
- реализован CRUD для модели поставщика
- настроены права доступа (permissions): 
-- только активные сотрудники имеют доступ к API;
-- запрещены обновление через API поля «Задолженность перед поставщиком»;
- добавлена возможность через API фильтрации объектов по определенной стране.




### Требования


### Установка зависимостей

[tool.poetry]
name = "online-tech-store"
version = "0.1.0"
description = ""
authors = ["Bazavod <eugeny.bazavod@list.ru>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = "^5.2.6"
pandas = "^2.3.2"
requests = "^2.32.5"
openpyxl = "^3.1.5"
python-dotenv = "^1.1.1"
pytest = "^8.4.2"
pytest-cov = "^7.0.0"
psycopg2-binary = "^2.9.10"
pillow = "^11.3.0"
ipython = "^9.5.0"
redis = "^6.4.0"
djangorestframework-simplejwt = "^5.5.1"
django-filter = "^25.1"
coverage = "^7.10.6"
gunicorn = "^23.0.0"
black = "^25.1.0"
isort = "^6.0.1"
flake8 = "^7.3.0"

[tool.poetry.group.lint.dependencies]
black = "^25.1.0"
isort = "^6.0.1"
flake8 = "^7.3.0"

[tool.black]
line-length = 160
exclude = '''(\.git)'''

[tool.isort]
line_length = 119

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

### Запуск Development сервера


### Создание билда


## Тестирование



## Deploy и CI/CD


## Contributing

## FAQ 

### Зачем вы разработали этот проект?


## To do

## Команда проекта

- [Евгений Базавод]  back-end developer

## Источники
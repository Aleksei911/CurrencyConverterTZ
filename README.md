# CurrencyConverterTZ

## Базовые технологии проекта

- Python 3.11
- Django 4.2.5
- Docker Desktop

#### Создание образов:

```bash
docker-compose build
```

#### Запуск приложения

```bash
docker-compose up
```

#### Внешние порты

- 8000:8000


#### Описание задания

Тестовое задание

Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
Ответ:
{

"result": 62.16

}
Любой фреймворк в пределах python.
Данные о текущих курсах валют необходимо получать с внешнего сервиса.
Контейнерезация, документация, и прочее — приветствуется.»

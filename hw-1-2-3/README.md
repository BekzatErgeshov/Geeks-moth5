# DRF API Project

Небольшой Django REST Framework проект с API для товаров, калькулятора и проверки температуры.

## Запуск проекта

1. Установить зависимости:

```powershell
pip install -r requirements.txt
```

2. Применить миграции:

```powershell
python manage.py migrate
```

3. Запустить сервер:

```powershell
python manage.py runserver
```

После запуска проект будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

## Админка

Адрес админки:

```text
http://127.0.0.1:8000/admin/
```

Логин:

```text
admin
```

Пароль:

```text
admin1234
```

## API

Базовый путь:

```text
http://127.0.0.1:8000/api/v1/
```

### Список категорий

```text
GET /api/v1/category-list
```

### Список продуктов

```text
GET /api/v1/product-list
```

### Калькулятор

```text
POST /api/v1/calculator
```

Пример запроса:

```json
{
  "first_value": 10,
  "second_value": 5,
  "operator": "+"
}
```

Доступные операторы:

```text
+  -  *  /
```

### Температура

```text
POST /api/v1/temperature
```

Пример запроса:

```json
{
  "temperature": 30
}
```

Типы температуры:

```text
-10 до +10  -> низкая температура
+10 до +25  -> нормальная температура
+25 до +40  -> очень жарко
```

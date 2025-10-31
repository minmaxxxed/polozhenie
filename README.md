# Polozhenie

## Запуск приложения

1. Создать файл `.env` в корневой папке (пример в `.env.example`)
2. Поднять сервисы:

```shell
docker compose up --build -d
```
## Настройка pre-commit-hooks
### Установка
1. Установить pre-commit
```shell
pip install pre-commit
```
2. Установить pre-commit-hooks
```shell
pre-commit install
```
### Использование
Проверка файлов коммита
```shell
pre-commit run
```
Проверка всех файлов репозитория:
```shell
pre-commit run --all-files
```

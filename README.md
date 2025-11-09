# Polozhenie

## Зависимости

- python ≥ 3.13
- docker
- docker-compose
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [pre-commit](https://pre-commit.com/)

## Запуск приложения

1. Создать файл `.env` в корневой папке (пример заполнения в `.env.example`)
2. Поднять сервисы:

```shell
docker compose --profile services --profile infra up --build
```

## Настройка dev-окружения

### Ручная проверка качества кода

Проверка отдельного сервиса/директории:

```shell
make -C <имя-директории> check
```

Внесение автоматических изменений:

```shell
make -C <имя-директории> fix
```

Для python-проектов можно использовать синтаксис uv run:

```shell
uv run --directory=<имя-директории> make check
uv run --directory=<имя-директории> make fix
```

### pre-commit-hooks

Установка pre-commit-hooks:
```shell
pre-commit install --install-hooks
```

Проверка файлов коммита:
```shell
pre-commit run
```

Проверка всех файлов репозитория:
```shell
pre-commit run --all-files
```

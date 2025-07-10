# market_backend

### Технологии
- python3.12
- FASTAPI 
- poetry 
- Ruff 
### Используемые API


### Задача
- Выполнить бекенд проекта
- ROAD MAP 
- деплой CI/CD
- Выбор лицензии распостронения 


### Запуск проекта

## Холодный старт
- poetry init -n --python "^3.12"
- poetry config virtualenvs.in-project true
- poetry env use python3.12
- mkdir src
- poetry install --no-root

## Установка требует
  * python3.12
    * poetry
        * ##### Linux/macOS
        - *      curl -sSL https://install.python-poetry.org | python3 -
        * ##### Windows (PowerShell)
        - *     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        * ### Oсновные команды poetry
          #### Активировать окружение
          - poetry shell
          #### Добавить новую зависимость
          - poetry add package-name
          #### Обновить зависимости
          - poetry update
          #### Запустить приложение
          - poetry run python src/main.py 
          #### Форматировать код
          - poetry run format
          #### Проверить и исправить код
          - poetry run lint
<h1 align="center">🤖🧪 Автотесты UI & API | Python + Pytest + Selenium + Requests</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pytest-8.3-green?logo=pytest" alt="Pytest">
  <img src="https://img.shields.io/badge/Selenium-latest-brightgreen?logo=selenium" alt="Selenium">
  <img src="https://img.shields.io/badge/Requests-HTTP-orange?logo=fastapi" alt="Requests">
</p>

---

## 📌 Описание проекта
Проект закрытый для POST запросов, но GET можно выполнять без токена: [pokemonbattle.ru](https://pokemonbattle.ru/)

В данном репозитории представлены **автоматизированные тесты** для проверки:
- 🌐 **UI**: авторизация и функциональность на сайте [pokemonbattle-stage.ru](https://pokemonbattle-stage.ru) с помощью **Selenium WebDriver**  
- 🔗 **API**: работа с REST API (создание, изменение и действия с покемонами) через библиотеку **Requests**

Все тесты запускаются под управлением **Pytest**, с возможностью параметризации, фикстур и интеграции с отчётами.

---

## ⚙️ Стек технологий
- 🐍 **Python 3.12**  
- 🧪 **Pytest** (юнит и интеграционные тесты)  
- 🌍 **Selenium WebDriver** (UI автотесты)  
- 📡 **Requests** (API тесты)  
- 📊 **Allure** (репорты и визуализация результатов)  

---

## ✅ Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## 🖼 Скриншоты

### Pytest список собранных тестов

![image](https://raw.githubusercontent.com/MaximOlesov/Python_Pytest_Requests_Selenium/refs/heads/main/screenshots/Pytest-api.png)

Запуск тестов через **Pytest**. Фреймворк собирает тестовые функции и готовит их к выполнению — отображается список найденных тестов с путями к файлам. Это подтверждает корректную структуру проекта и наличие рабочих автотестов.

---

### Запуска UI-теста Selenium
![image](https://raw.githubusercontent.com/MaximOlesov/Python_Pytest_Requests_Selenium/refs/heads/main/screenshots/Python-web.png)

Авторизации на сайте **pokemonbattle-stage.ru** через **Selenium WebDriver**. Тест открывает браузер, вводит email и пароль, и проверяет успешный вход.

---

### Запуска API-теста Requests + Pytest
![image](https://raw.githubusercontent.com/MaximOlesov/Python_Pytest_Requests_Selenium/refs/heads/main/screenshots/Requests-api.png)

Тесты REST API с помощью библиотеки **Requests**. Проверяется корректность кода ответа, имя тренера и параметры в JSON-ответе.

---

### Успешное выполнение тестов Pytest
![image](https://raw.githubusercontent.com/MaximOlesov/Python_Pytest_Requests_Selenium/refs/heads/main/screenshots/passedtests.png)

Итог выполнения тестов через **Pytest**. Все тесты завершились успешно ✔️

## 💻 Локальный запуск тестов из терминала
1. Скачать проект
2. Перейти через терминал в директорию проекта
2. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.

Далее команды для MacOS (инструкция для Windows [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```

``` markdown
python3 -m pip install selenium
```

``` markdown
python3 -m pip install allure-pytest
```

5. Запускаем
``` markdown
pytest tests/test_pokemons.py
```

Ожидаемый результат: получим отчет о прохождении тестов.


**👤 Автор:**

Максим Олесов ([@Mxwave](https://t.me/Mxwave))

<p align="left">
  <img src="https://img.shields.io/badge/Made%20by-Maxim%20Olesov-blue?style=for-the-badge&logo=github" alt="Made by Maxim Olesov" />
</p>

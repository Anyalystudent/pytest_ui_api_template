# pytest_ui_api_template

## Автоматизации тестирования сайта Деливери - быстрая доставка

### Шаги

1. Склонировать проект 'git clone https://github.com/Anyalystudent/pytest_ui_api_template.git
2. Установить зависимости 'pip install > -r requirements.txt'
3. Запустить все тесты 'pytest'
4. Запустить api тесты 'pytest test/test_api.py'. В api тестах используется переменная COOKIES,
   которая вынесена в отдельный файл cookies.py. Файл cookies.py добавлен в .gitignore.
5. Запустить ui тесты 'pytest test/test_ui.py'. При запуске тестов появляется капча,
   необходимо ее пройти вручную
6. Сгенерировать отчет 'allure generate allure-files -o allure-report'
7. Открыть отчет 'allure open allure-report'

### Стек:

- pytest
- selenium
- requests
- allure
- json

### Структура:

- ./test - тесты
- ./pages - описание страниц
- ./allure-files - сгенерированные файлы отчета
- ./allure-report - отчет

### Полезные ссылки

- [Сайт] (https://market-delivery.yandex.ru/)
- [Финальный проект по ручному тестированию] (https://luzanovaamqa123skypro.yonote.ru/share/7ae2430c-d99a-491b-89d8-6439f9d8d880)

### Библиотеки

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
Для начала нужно установить пакеты

    pip install -r requirements.txt

Функция encode кодирует строку в соответсвие с таблицей азбуки Морзе.
Для запуска тестов выполните в консоли:

    python -m doctest -v doctest.txt
    
Функция encode декодирует строку из азбуки Морзе в английский.
Для запуска тестов выполните в консоли:

    python -m pytest morse.py
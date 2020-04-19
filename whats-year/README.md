Для начала нужно установить пакеты

    pip install -r requirements.txt

Функция what_is_year_now возвращает текущий год.

Для запуска теста выполните в консоли:

    python -m unittest what_is_year_now.py
    
Чтобы получить отчет о покрытии запустите:

     coverage run -m unittest what_is_year_now.py 
     
     coverage html
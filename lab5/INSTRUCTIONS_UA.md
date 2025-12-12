# Інструкція з запуску Lab 5

## 1. Налаштування бази даних

Необхідно створити базу даних та таблиці. Виконайте наступні SQL скрипти у вказаному порядку. 
Ви можете зробити це через MySQL Workbench або командний рядок.

**Порядок виконання:**
1. `lab_1_shema.sql` (Створює базу `maksim_rental` та основні таблиці)
2. `lab_5(1part).sql` (Додає таблицю UserNotes та тригери)
3. `lab_5_CalculateProcedure.sql` (Додає збережену процедуру)
4. `lab_5_triggers.sql` (Додає додаткові тригери валидації)

**Команди для терміналу (якщо встановлено MySQL):**
```bash
mysql -u root -p < lab_1_shema.sql
mysql -u root -p < "lab_5(1part).sql"
mysql -u root -p < lab_5_CalculateProcedure.sql
mysql -u root -p < lab_5_triggers.sql
```

## 2. Налаштування Python проекту

Перейдіть у папку `lab5`:
```bash
cd lab5
```

**Налаштування конфігурації:**
Відкрийте файл `main.py` та переконайтесь, що налаштування бази даних відповідають вашим (особливо пароль):
```python
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ВАШ_ПАРОЛЬ' # Змініть 'password' на ваш реальний пароль MySQL
```

**Встановлення бібліотек:**
Рекомендується використовувати віртуальне середовище:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

Встановіть залежності:
```bash
pip install -r requirements.txt
```

## 3. Запуск

Запустіть додаток:
```bash
python main.py
```

Додаток буде доступний за адресою: `http://127.0.0.1:5000`

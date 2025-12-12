# Розгортання на Azure (Deployment Guide)

Цей файл містить покрокову інструкцію для розгортання вашого проекту в Microsoft Azure з налаштуванням CI/CD через GitHub.

## 1. Підготовка локального середовища
Ми вже додали підтримку Swagger та змінних оточення. Вам потрібно лише оновити бібліотеки:

```powershell
# У папці lab5 (з активованим venv)
pip install -r requirements.txt
```

Перевірте, що додаток запускається локально:
```powershell
python main.py
```
Відкрийте Swagger (документацію): `http://127.0.0.1:5000/apidocs/`  
(Якщо бачите гарну сторінку з документацією API — все супер!)

---

## 2. Завантаження коду на GitHub
Щоб налаштувати автоматичне розгортання (CI/CD), ваш код має бути на GitHub.

1.  **Ініціалізація Git (якщо ще не зроблено):**
    Відкрийте термінал у корені проекту (`maksim_database-main`) і виконайте:
    ```bash
    git init
    # Додаємо всі файли
    git add .
    git commit -m "Initial commit with Lab 5 and Cloud setup"
    ```

2.  **Створення репозиторію на GitHub:**
    *   Зайдіть на [github.com](https://github.com) і створіть новий **публічний** репозиторій.
    *   Назвіть його, наприклад, `rental-system-cloud`.

3.  **Зв'язування та завантаження:**
    Замініть `URL_ВАШОГО_РЕПОЗИТОРІЮ` на посилання, яке дав GitHub (наприклад, `https://github.com/ВашНік/rental-system-cloud.git`):
    ```bash
    git remote add origin URL_ВАШОГО_РЕПОЗИТОРІЮ
    git branch -M main
    git push -u origin main
    ```

---

## 3. Створення Azure Web App

1.  Зайдіть на [Azure Portal](https://portal.azure.com).
2.  Натисніть **"Create a resource"** -> **"Web App"**.
3.  **Налаштування:**
    *   **Subscription:** Ваша студентська підписка.
    *   **Resource Group:** Створіть нову (наприклад, `rental-lab5-rg`).
    *   **Name:** Унікальне ім'я (наприклад, `maksim-rental-app`).
    *   **Publish:** `Code`.
    *   **Runtime stack:** `Python 3.10` (або новіший).
    *   **Region:** `West Europe` (або будь-який ближчий).
    *   **Pricing Plan:** Оберіть `Free F1` (для студентів) або `Basic B1`.
4.  Натисніть **Review + create** -> **Create**.

---

## 4. Налаштування бази даних (Azure Database for MySQL)

*Оскільки Azure for MySQL не завжди безкоштовний, ви можете використовувати **локальну SQLite** для тесту або спробувати створити "Azure Database for MySQL flexible server" (іноді є безкоштовний ліміт).*

Якщо ви хочете просто здати, часто достатньо "Azure SQL" або просто показати, що код вміє підключатись. Але для повноцінної роботи треба створити MySQL в Azure:
1.  У пошуку Azure знайдіть **"Azure Database for MySQL flexible server"**.
2.  Створіть сервер (оберіть "Development" або "Burstable" тариф B1s для економії).
3.  Після створення зайдіть у налаштування та **дозвольте доступ до Azure Services** у Firewall.

---

## 5. Налаштування змінних середовища (Configuration)

Щоб сайт знав паролі від бази:
1.  У вашому Web App в меню зліва оберіть **Configuration** -> **Environment variables**.
2.  Натисніть **+ Add** і додайте:
    *   `MYSQL_HOST`: (адреса вашого Azure MySQL серверу)
    *   `MYSQL_USER`: (ім'я адміна)
    *   `MYSQL_PASSWORD`: (пароль який ви придумали при створенні бази)
    *   `MYSQL_DB`: `maksim_rental`
    *   `SCM_DO_BUILD_DURING_DEPLOYMENT`: `true`
3.  Натисніть **Save**.

---

## 6. Налаштування Deployment (CI/CD)

1.  У вашому Web App в меню зліва зайдіть у **Deployment Center**.
2.  **Source:** `GitHub`.
3.  Авторизуйтесь через GitHub.
4.  Оберіть ваш репозиторій `rental-system-cloud` і гілку `main`.
5.  Натисніть **Save**.

Azure автоматично створить файл workflow і почне розгортання. Через 5-10 хвилин ваш сайт буде доступний за посиланням `https://maksim-rental-app.azurewebsites.net`.

---

## 7. Перевірка
Зайдіть на `https://ВАШ-САЙТ.azurewebsites.net/apidocs/` — ви маєте побачити інтерфейс Swagger.

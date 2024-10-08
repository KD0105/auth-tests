# Rostelecom Authentication Test Suite

Этот репозиторий содержит набор автоматизированных тестов для проверки системы аутентификации Rostelecom. Тесты написаны с использованием Selenium и Pytest и предназначены для проверки различных сценариев входа и безопасности.

## Содержание

- [Описание проекта](#описание-проекта)
- [Тестовые сценарии](#тестовые-сценарии)
- [Требования](#требования)
- [Установка](#установка)



## Описание проекта

Этот проект реализует автоматизированные тесты для проверки функциональности аутентификации на веб-сайте Rostelecom. Основное внимание уделяется проверке корректности входа, обработки ошибок и безопасности.

## Тестовые сценарии

Тесты покрывают следующие сценарии:

1. Успешная аутентификация с корректными данными.
2. Попытка входа с некорректными учетными данными.
3. Попытка входа с пустыми полями логина и пароля.
4. Проверка успешного редиректа после входа.
5. Проверка обработки некорректного client_id.
6. Проверка обработки некорректного redirect_uri.
7. Аутентификация с различными значениями scope.
8. Проверка state параметра в URL.
9. Защита от SQL-инъекций в поле логина.
10. Проверка производительности аутентификации.
11. Редирект с HTTP на HTTPS.
12. Попытка входа в заблокированный аккаунт.
13. Доступность страницы входа.
14. Проверка страницы на наличие необходимых элементов.
15. Проверка обработки ошибок для неверного состояния.

## Требования

- Python 3.7+
- Selenium
- Pytest
- Установленный веб-драйвер для используемого браузера (например, ChromeDriver для Chrome)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/KD0105/auth-tests.git
   cd auth-tests

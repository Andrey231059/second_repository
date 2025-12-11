# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
# import random
# import time
#
# browser = webdriver.Firefox()
# #Открываем стартовую страницу браузера
# browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# assert "Википедия" in browser.title
#
# #Вводим в поле поиска заданную пользователем тему
# search_box = browser.find_element(By.ID, "searchInput")
# Tema = str(input("Введите интересующую Вас тему"))
# search_box.send_keys(Tema)
#
# search_box.send_keys(Keys.RETURN)
# time.sleep(5)
#
# #Находим все найденные страницы по этому поиску и открываем случайную
# hatnotes = []
# for element in browser.find_elements(By.TAG_NAME, "div"):
#     cl = element.get_attribute("class")
#     if cl == "mw-search-result-heading":
#         hatnotes.append(element)
#
# print(f"Найдено {len(hatnotes)} результатов")
# if len(hatnotes) > 0:
#     #Выбираем случайный вариант
#     hatnote = random.choice(hatnotes)
#     print("Выбранный результат:",hatnote.text)
#     #Получаем ссылку на статью
#     link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
#     # Переходим по ссылке
#     browser.get(link)
#     time.sleep(5)
# else:
#     print("Результаты не найдены.")
#     browser.quit()
#
# # Теперь будем выполнять задание
# # 1. Спрашивать у пользователя первоначальный запрос.
# #
# # 2. Переходить по первоначальному запросу в Википедии.
# #
# # 3. Предлагать пользователю три варианта действий:
# #
# # листать параграфы текущей статьи;
# # перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# # - листать параграфы статьи;
# #
# # - перейти на одну из внутренних статей.
# #
# # выйти из программы.
# # В поле для ответа загрузи ссылку на Git.
# Var = int(input("Что желаете: 1-листать параграфы текущей статьи, 2-перейти на одну из связанных страниц, 3-выйти"))
# if Var == 1:
#     paragraphs = browser.find_elements(By.TAG_NAME, "p")
#     # Для перебора пишем цикл
#     for paragraph in paragraphs:
#         print(paragraph.text)
#         input()
#
# elif Var == 2:
#     hatnotes = []
#     for element in browser.find_elements(By.TAG_NAME, "div"):
#         cl = element.get_attribute("class")
#         if cl == "hatnote navigation-not-searchable ts-main":
#             hatnotes.append(element)
#     print(f"Найдено {len(hatnotes)} результатов")
#     if len(hatnotes) > 0:
#
#         hatnote = random.choice(hatnotes)
#         print(hatnote.text)
#         link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
#         browser.get(link)
#         Var2 = int(input("Что желаете: 1-листать параграфы текущей статьи, 2-выйти"))
#         if Var == 1:
#             paragraphs = browser.find_elements(By.TAG_NAME, "p")
#             # Для перебора пишем цикл
#             for paragraph in paragraphs:
#                 print(paragraph.text)
#                 input()
#         else:
#             browser.quit()
#     else:
#         print("Результаты не найдены.")
#         browser.quit()
# else:
#     browser.quit()


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/kaluga/category/svet"
driver.get(url)
time.sleep(5)

luminaires = driver.find_elements(By.CLASS_NAME, 'ProductCardMain_card__KQzzn')
print(luminaires)
print(f"Найдено товаров: {len(luminaires)}")
parsed_data = []

for luminaire in luminaires:
    try:

        title = luminaire.find_element(By.CLASS_NAME, 'ProductName').text
        # price = luminaire.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU')
        # # price = luminaire.find_element(By.CSS_SELECTOR, 'span[data-testid="price"]::text')
        # link = luminaire.find_element(By.CLASS_NAME, 'MainInfo_wrapper__GthSf').get_attribute('href')
        # title = luminaire.find('div', itemprop='name').get_text(strip=True)
        # price = luminaire.find('span', {'data-testid': 'price'}).get_text(strip=True)
        # link = luminaire.find('a', href=True)['href']
        # print(title, price, link)
        # parsed_data.append([title, price, link])
        parsed_data.append([title])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    # parsed_data.append([title])

driver.quit()

with open("lum.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)

# import csv
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.divan.ru/kaluga/category/svet"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)  # Должно быть 200
# print(len(response.text))    # Если < 1000 — скорее всего, защита
# print(response.text[:1000])  # Посмотри, что пришло
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Находим все карточки товаров
# luminaires = soup.find_all('div', class_='ProductCardMain')
#
# parsed_data = []
#
# for luminaire in luminaires:
#     try:
#         title = luminaire.find('div', itemprop='name').get_text(strip=True)
#         price = luminaire.find('span', {'data-testid': 'price'}).get_text(strip=True)
#         link = luminaire.find('a', href=True)['href']
#         print(title, price, link)
#         parsed_data.append([title, price, link])
#
#     except Exception as e:
#         print(f"Ошибка при парсинге: {e}")
#
# with open("lum.csv", 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Название светильника', 'Цена', 'Ссылка на товар'])
#     writer.writerows(parsed_data)

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# import time
# import csv
#
# # Настройка браузера
# service = Service("geckodriver.exe")
# options = Options()
# # options.add_argument("--headless")  # Работать без GUI
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.set_preference("general.useragent.override",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#
# driver = webdriver.Firefox(options=options)
#
# url = "https://www.divan.ru/kaluga/category/svet"
#
# try:
#     driver.get(url)
#     time.sleep(5)  # Ждём, пока загрузятся товары
#
#     luminaires = driver.find_elements(By.CSS_SELECTOR, 'div.ProductCardMain')
#     print(f"Найдено товаров: {len(luminaires)}")
#
#     parsed_data = []
#     for luminaire in luminaires:
#         try:
#             title = luminaire.find_element(By.CSS_SELECTOR, 'div[itemprop="name"]').text
#             price = luminaire.find_element(By.CSS_SELECTOR, 'span[data-testid="price"]').text
#             link = luminaire.find_element(By.TAG_NAME, 'a').get_attribute('href')
#             parsed_data.append([title, price, link])
#             print(title)
#         except Exception as e:
#             print(f"Ошибка при парсинге элемента: {e}")
#             continue
#
#     # Сохранение в CSV
#     with open("lum.csv", 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Название светильника', 'Цена', 'Ссылка на товар'])
#         writer.writerows(parsed_data)
#
# except Exception as e:
#     print(f"Ошибка при загрузке страницы: {e}")
#
# finally:
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# import time
# import csv
#
# # Указываем путь к geckodriver.exe
# service = Service('./geckodriver.exe', timeout=60)
#
# options = Options()
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument("--disable-web-security")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-background-timer-throttling")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.set_preference("general.useragent.override",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#
# driver = webdriver.Firefox(service=service, options=options)
#
# url = "https://www.divan.ru/kaluga/category/svet"
#
# try:
#     driver.get(url)
#     time.sleep(5)  # Ждём загрузки JS
#
#     luminaires = driver.find_elements(By.CSS_SELECTOR, 'div.ProductCardMain')
#     print(f"Найдено товаров: {len(luminaires)}")
#
#     parsed_data = []
#     for luminaire in luminaires:
#         try:
#             title = luminaire.find_element(By.CSS_SELECTOR, 'div[itemprop="name"]').text
#             price = luminaire.find_element(By.CSS_SELECTOR, 'span[data-testid="price"]').text
#             link = luminaire.find_element(By.TAG_NAME, 'a').get_attribute('href')
#             parsed_data.append([title, price, link])
#             print(title)
#         except Exception as e:
#             print(f"Ошибка при парсинге элемента: {e}")
#             continue
#
#     # Сохранение в CSV
#     with open("lum.csv", 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Название светильника', 'Цена', 'Ссылка на товар'])
#         writer.writerows(parsed_data)
#
# except Exception as e:
#     print(f"Ошибка при загрузке страницы: {e}")
#
# finally:
#     driver.quit()

#Код, написанный с использованием новых селекторов.
#


#Код, написанный с использованием новых селекторов.
# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# url = "https://tomsk.hh.ru/vacancies/programmist"
# driver.get(url)
# time.sleep(3)
#
# vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')
#
# parsed_data = []
#
# for vacancy in vacancies:
#     try:
#         title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2')
#         title = title_element.text
#         link = title_element.get_attribute('href')
#         company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
#
#         try:
#             salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
#         except:
#             salary = "Не указана"
#
#     except Exception as e:
#         print(f"Произошла ошибка при парсинге: {e}")
#         continue
#
#     parsed_data.append([title, company, salary, link])
#
# driver.quit()
#
# with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
#     writer.writerows(parsed_data)

# #Код, написанный экспертом в уроке.
# # Импортируем модуль со временем
# import time
# # Импортируем модуль csv
# import csv
# # Импортируем Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # Инициализируем браузер
# driver = webdriver.Firefox()
# # Если мы используем Chrome, пишем
# # driver = webdriver.Chrome()
#
# # В отдельной переменной указываем сайт, который будем просматривать
# url = "https://tomsk.hh.ru/vacancies/programmist"
#
# # Открываем веб-страницу
# driver.get(url)
#
# # Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
# time.sleep(3)
#
# # Находим все карточки с вакансиями с помощью названия класса
# # Названия классов берём с кода сайта
# vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VIUF0yM')
#
# # Выводим вакансии на экран
# print(vacancies)
# # Создаём список, в который потом всё будет сохраняться
# parsed_data = []
# print(len(vacancies))
# # Перебираем коллекцию вакансий
# # Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
# for vacancy in vacancies:
#     try:
#         # Находим элементы внутри вакансий по значению
#         # Находим названия вакансии
#         title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_7-0-4').text
#         # Находим названия компаний
#         company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text_typography-label-3-regular___Nhtlp_4-4-2').text
#         # Зарплата — через data-qa (надёжнее всего!)
#         try:
#             salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_4-4-2').text
#             # salary = vacancy.find_element(By.XPATH, './/span[contains(text(), "₽")]').text
#             # salary_container = vacancy.find_element(By.CSS_SELECTOR, 'div.narrow-container--HaV4hduxPuElpx0V')
#             # salary = salary_container.text.strip()
#             # salary_element = WebDriverWait(vacancy, 5).until(
#             #     EC.presence_of_element_located((By.XPATH, './/span[contains(text(), "₽")]'))
#             # )
#             # salary = salary_element.text.strip()
#         except:
#             salary = "Не указана"
#         # Находим ссылку с помощью атрибута 'href'
#         link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_7-0-4').get_attribute('href')
#         # parsed_data.append([title, company, salary, link])
#         parsed_data.append([title, company, salary, link])
#     # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
#     except:
#         print("произошла ошибка при парсинге")
#     continue
#
#     # Вносим найденную информацию в список
#     parsed_data.append([title, company, salary, link])
#
# # Закрываем подключение браузер
# driver.quit()
#
# # Прописываем открытие нового файла, задаём ему название и форматирование
# # 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
# with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
#     # Используем модуль csv и настраиваем запись данных в виде таблицы
#     # Создаём объект
#     writer = csv.writer(file)
#     # Создаём первый ряд
#     writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
#     # Прописываем использование списка как источника для рядов таблицы
#     writer.writerows(parsed_data)

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv
#
# # Настройка браузера
# service = Service('./geckodriver.exe')
# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.set_preference("general.useragent.override",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#
# driver = webdriver.Firefox(service=service, options=options)
#
# url = "https://tomsk.hh.ru/search/vacancy?text=программист&area=113"
#
# try:
#     driver.get(url)
#     time.sleep(5)  # Ждём загрузки JS
#
#     vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VlUf0yM')
#
#     parsed_data = []
#     for vacancy in vacancies:
#         try:
#             title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIL_7-0-4').text
#             company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text__typography-label-3-regular___NhHp_4-4-2').text
#             link = vacancy.find_element(By.TAG_NAME, 'a').get_attribute('href')
#
#             # Переходим на страницу вакансии
#             driver.get(link)
#             time.sleep(3)  # Ждём загрузки
#
#             # На странице вакансии находим зарплату
#             try:
#                 salary_element = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.compensation-labels'))
#                 )
#                 salary = salary_element.text.strip()
#             except:
#                 salary = "Не указана"
#
#             parsed_data.append([title, company, salary, link])
#             print(title, salary)
#         except Exception as e:
#             print(f"Ошибка при парсинге вакансии: {e}")
#             continue
#
#     # Сохранение в CSV
#     with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
#         writer.writerows(parsed_data)
#
# except Exception as e:
#     print(f"Ошибка при загрузке страницы: {e}")
#
# finally:
#     driver.quit()
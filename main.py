from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import random
import time

browser = webdriver.Firefox()
#Открываем стартовую страницу браузера
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title

#Вводим в поле поиска заданную пользователем тему
search_box = browser.find_element(By.ID, "searchInput")
Tema = str(input("Введите интересующую Вас тему"))
search_box.send_keys(Tema)

search_box.send_keys(Keys.RETURN)
time.sleep(5)

#Находим все найденные страницы по этому поиску и открываем случайную
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "mw-search-result-heading":
        hatnotes.append(element)

print(f"Найдено {len(hatnotes)} результатов")
if len(hatnotes) > 0:
    #Выбираем случайный вариант
    hatnote = random.choice(hatnotes)
    print("Выбранный результат:",hatnote.text)
    #Получаем ссылку на статью
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    # Переходим по ссылке
    browser.get(link)
    time.sleep(5)
else:
    print("Результаты не найдены.")
    browser.quit()

# Теперь будем выполнять задание
# 1. Спрашивать у пользователя первоначальный запрос.
#
# 2. Переходить по первоначальному запросу в Википедии.
#
# 3. Предлагать пользователю три варианта действий:
#
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
#
# - перейти на одну из внутренних статей.
#
# выйти из программы.
# В поле для ответа загрузи ссылку на Git.
Var = int(input("Что желаете: 1-листать параграфы текущей статьи, 2-перейти на одну из связанных страниц, 3-выйти"))
if Var == 1:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

elif Var == 2:
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    print(f"Найдено {len(hatnotes)} результатов")
    if len(hatnotes) > 0:

        hatnote = random.choice(hatnotes)
        print(hatnote.text)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        Var2 = int(input("Что желаете: 1-листать параграфы текущей статьи, 2-выйти"))
        if Var == 1:
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            # Для перебора пишем цикл
            for paragraph in paragraphs:
                print(paragraph.text)
                input()
        else:
            browser.quit()
    else:
        print("Результаты не найдены.")
        browser.quit()
else:
    browser.quit()
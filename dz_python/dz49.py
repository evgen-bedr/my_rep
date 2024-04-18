# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.
import requests
from bs4 import BeautifulSoup


class url_parser:
    def __init__(self, link):
        self.link = link

    def request_url(self):
        try:
            response = requests.get(self.link)
            if response.status_code == 200:
                return response
            else:
                print(f'Сайт {self.link} не доступен')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Ошибка подключения к сайту {self.link}')
            return None

    def get_a(self):
        response = self.request_url()
        if response is not None:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all("a")
            all_links = []
            for i in links:
                href = i.get("href")
                if href:
                    all_links.append(href)
            return all_links
        else:
            return []


user_url = 'https://cnn.com'

url = url_parser(user_url)
print(url.get_a())


# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
import requests
from bs4 import BeautifulSoup


class url_parser:
    def __init__(self, link, h_tag):
        self.link = link
        self.h_tag = h_tag

    def request_url(self):
        try:
            response = requests.get(self.link)
            if response.status_code == 200:
                return response
            else:
                print(f'Сайт {self.link} не доступен')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Ошибка подключения к сайту {self.link}')
            return None

    def get_a(self):
        response = self.request_url()
        if response is not None:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            h_tags = soup.find_all(self.h_tag)
            for i in h_tags:
                if i.text.strip():
                    yield (i.text.strip())
                else:
                    continue

        else:
            return []


user_url = 'https://cnn.com'
user_h = 'h2'

url = url_parser(user_url, user_h)
generator = url.get_a()
for i in generator:
    print(i)

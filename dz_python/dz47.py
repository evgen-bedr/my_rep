# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу
# и возвращает объект ответа. Затем выведите следующую информацию об ответе:
#
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
#
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
#
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

import requests


def get_response(url):
    return requests.get(url)


url = "https://example.com"
response = get_response(url)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)

# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов
# и возвращает список наиболее часто встречающихся слов на веб-страницах.
# Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET
# и использовать регулярные выражения для извлечения слов.
# Затем функция должна подсчитать количество вхождений каждого слова
# и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.

import requests
import re


def find_common_words(url_list):
    for link in url_list:
        pattern = r'"articleBody":"(.+)","articleSection"'
        get_link = requests.get(link)
        parsed_text = re.findall(pattern, get_link.text)
        words = parsed_text[0].lower().split()

        hashmap = {}
        for i in words:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        top_ten_words = sorted_items[:10]
        top_ten_words = ', '.join(f'{word}: {count}' for word, count in top_ten_words)
        yield f'{top_ten_words} - {link}'


urls = [
    'https://edition.cnn.com/2024/04/10/politics/trump-chaos-johnson-abortion/index.html',
    'https://edition.cnn.com/2024/04/11/europe/ukraine-power-plant-destroyed-russia-intl/index.html',
    'https://edition.cnn.com/2024/04/11/climate/bogota-water-rationing-drought-climate-intl/index.html',
    'https://edition.cnn.com/2024/04/11/asia/myanmar-myawaddy-knu-military-junta-intl-hnk/index.html',
    'https://edition.cnn.com/2024/04/11/australia/australia-drugs-meth-mexican-cartels-intl-hnk/index.html',
    'https://edition.cnn.com/travel/tsa-firearm-interceptions-airports-january-march-2024/index.html',
    'https://edition.cnn.com/2024/04/11/health/bird-flu-virus-wellness/index.html',
    'https://edition.cnn.com/2024/04/11/sport/mondo-duplantis-pole-vault-paris-olympics-spt-intl/index.html',
    'https://edition.cnn.com/2024/03/23/sport/figure-skating-championships-deanna-stellato-dudek/index.html',
    'https://edition.cnn.com/2024/03/24/sport/ilia-malinin-wins-first-world-title-figure-skating-spt-intl/index.html'
]

for result in find_common_words(urls):
    print(result)

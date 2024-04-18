# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.
#
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)
# Вывод: ['info@example.com', 'support@example.com']

import re


def extract_emails(text):
    pattern = r"\b[a-z-_0-9]+@[a-z0-9-]+\.[a-z]+\b"
    result = re.findall(pattern, text)
    return result


text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)

# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
#
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
#
# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."


import re


def highlight_keywords(text, keywords):
    for i in keywords:
        pattern = r"\b" + i + r"\b"
        text = re.sub(pattern, lambda x: '*' + x.group(0) + '*', text, flags=re.IGNORECASE)
    return text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)

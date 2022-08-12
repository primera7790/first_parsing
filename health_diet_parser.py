import requests
from bs4 import BeautifulSoup
import json
import csv
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

accept = os.environ.get('ACCEPT')
user_agent = os.environ.get('USER-AGENT')

headers = {
    'Accept': accept,
    'User-Agent': user_agent
}

src = requests.get(url, headers=headers).text

with open('index.html', 'w', encoding='utf8') as file:
    file.write(src)

with open('index.html', encoding='utf8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

sections = soup.find_all(class_='mzr-block-header-light')
sections = sections[0:3]

count_sec = 1
for sec in sections:
    section_name = sec.text
    category_sec = sec.next_element.next_element.next_element.find_all(class_='mzr-tc-group-item-href')

    section_categories_list = {}
    for item in category_sec:
        category_name = item.text
        category_href = 'https://health-diet.ru' + item.get('href')
        section_categories_list[category_name] = category_href

    print(f'Работаю с секцией "{section_name}" ({count_sec}/3)')

    with open(f'{count_sec}. {section_name}.json', 'w', encoding='utf8') as file:
        json.dump(section_categories_list, file, indent=4, ensure_ascii=False)

    with open(f'{count_sec}. {section_name}.json', encoding='utf8') as file:
        categories_in_sec = json.load(file)

    count_sec += 1

    count_categories = 1
    for category_name, category_href in categories_in_sec.items():
        src = requests.get(url=category_href, headers=headers).text

        print(f'   ({count_categories}/{len(categories_in_sec)}) Заполняю категорию "{category_name}"...')

        with open(f'data/{section_name}/html/{count_categories}. {category_name}.html', 'w', encoding='utf8') as file:
            file.write(src)

        with open(f'data/{section_name}/html/{count_categories}. {category_name}.html', encoding='utf8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        alert_block = soup.find(class_='uk-alert-danger')
        if alert_block is not None:
            count_categories += 1
            continue

        table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
        product = table_head[0].text
        colories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text

        with open(f'data/{section_name}/{count_categories}. {category_name}.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    product,
                    colories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

        products_table = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
        products_list = []
        for item in products_table:
            products_tds = item.find_all('td')

            product = products_tds[0].find('a').text
            colories = products_tds[1].text
            proteins = products_tds[2].text
            fats = products_tds[3].text
            carbohydrates = products_tds[4].text

            products_list.append(
                {
                    'Product': product,
                    'Colories': colories,
                    'Proteins': proteins,
                    'Fats': fats,
                    'Carbohydrates': carbohydrates
                }
            )

            with open(f'data/{section_name}/json/{count_categories}. {category_name}.json', 'w', encoding='utf8') as file:
                json.dump(products_list, file,  indent=4, ensure_ascii=False)

            with open(f'data/{section_name}/{count_categories}. {category_name}.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        product,
                        colories,
                        proteins,
                        fats,
                        carbohydrates
                    ]
                )

        count_categories += 1

print("Работа завершена.")

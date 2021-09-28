import requests
from bs4 import BeautifulSoup
import json
import csv


# url = 'https://ford-mustang.infocar.ua/'
#
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open('index.html', 'w', encoding='UTF-8') as file:
#     file.write(src)

# with open('index.html', encoding='UTF-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_cars = soup.find_all(class_='d')
#
# all_cars_dict = {}
# for item in all_cars:
#     item_text0 = item('strong')[0].text
#     item_text1 = item('strong')[1].text
#     if item_text1 == '0':
#         item_text = f'{item_text0} 2017'
#     else:
#         item_text = f'{item_text0} {item_text1}'
#     item_href = 'http:' + item('a')[0].get('href')
#
#     all_cars_dict[item_text] = item_href
#
# with open('all_cars_dict.json', 'w') as file:
#     json.dump(all_cars_dict, file, indent=4, ensure_ascii=False)

with open('all_cars_dict.json') as file:
    all_cars = json.load(file)

count = 0
for car_name, car_href in all_cars.items():

    rep = ' '
    if rep in car_name:
        car_name = car_name.replace(rep, '_')

    req = requests.get(url=car_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{car_name}.html', 'w') as file:
        file.write(src)

    with open(f'data/{count}_{car_name}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    table_head = ['Motor', 'Power', 'KPP', 'Wheel_drive']

    with open(f'data/{count}_{car_name}.csv', 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(table_head)

    cars_data = soup.find_all(class_='tech-row')

    car_info = []
    for item in cars_data:
        motor = item.find(class_='td td-motor').text.strip()
        power = item.find(class_='td td-power').text.strip()
        kpp = item.find(class_='td td-kpp').text.strip()
        wheel_drive = item.find(class_='td td-privod').text.strip()

        car_info.append(
            {
                'Motor': motor,
                'Power': power,
                'KPP': kpp,
                'Wheel_drive': wheel_drive
            }
        )

        with open(f'data/{count}_{car_name}.csv', 'a') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (
                    motor,
                    power,
                    kpp,
                    wheel_drive
                )
            )

    with open(f'data/{count}_{car_name}.json', 'a', encoding='UTF-8') as file:
        json.dump(car_info, file, indent=4, ensure_ascii=False)

    count += 1

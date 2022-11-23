import os
import pandas as pd

txt_url = '../url_images.txt'


def read_csv():
    path_to_csv = r'../Data/buybookstoday_storeland_ru_goods_2022-11-15_12-57-29.csv'

    with open(path_to_csv, mode='r') as file:
        data = pd.read_csv(file, delimiter=";")
        dict_res = {'Название товара': [],
                    'Изображения товара': [],
                    'Цена продажи, без учёта скидок': [],
                    'Артикул': [],
                    'Полное описание товара': [],
                    'Скрыт ли товар на сайте?': [],
                    'Закупочная цена': [],
                    'Остаток': [],
                    'Название св-ва для модификации товара №1': [],
                    'Значение св-ва для модификации товара №1': [],
                    'Название св-ва для модификации товара №2': [],
                    'Значение св-ва для модификации товара №2': []}
        for name, price1, articul, show, price2, ostatok, key1, value1, key2, value2 in \
                zip(data['Название товара'],
                    data['Цена продажи, без учёта скидок'],
                    data['Пользовательский идентификатор товара'],
                    data['Скрыт ли товар на сайте?'],
                    data['Закупочная цена'],
                    data['Остаток'],
                    data['Название св-ва для модификации товара №1'],
                    data['Значение св-ва для модификации товара №1'],
                    data['Название св-ва для модификации товара №2'],
                    data['Значение св-ва для модификации товара №2']):
            dict_res['Название товара'].append(name)
            dict_res['Изображения товара'].append(find_url(int(articul)))
            dict_res['Цена продажи, без учёта скидок'].append(price1)
            dict_res['Артикул'].append(articul)
            dict_res['Полное описание товара'].append(find_description(str(articul)))
            if find_url(articul) != '':
                dict_res['Скрыт ли товар на сайте?'].append(0)
            else:
                dict_res['Скрыт ли товар на сайте?'].append(1)
            dict_res['Закупочная цена'].append(price2)
            dict_res['Остаток'].append(ostatok)
            dict_res['Название св-ва для модификации товара №1'].append(key1)
            dict_res['Значение св-ва для модификации товара №1'].append(value1)
            dict_res['Название св-ва для модификации товара №2'].append(key2)
            dict_res['Значение св-ва для модификации товара №2'].append(value2)

    res = pd.DataFrame(dict_res)
    res.to_csv('../Data/name_vs_imageUrl_rus.csv', mode='wb', encoding='windows-1251', index=False, sep=';')

def find_url(id_number: int) -> str:
    response = ''
    with open(txt_url, 'r') as urls:
        images = urls.readlines()
        for line in images:
            if f'/{id_number}.jpg' in line:
                response = line
            else:
                continue
    return response

def find_description(articul: str) -> str:
    for namedir in os.listdir('../Results'):
        if articul == int(namedir):
            filepath = os.path.join('../Results', namedir, 'description.txt')
            # print(os.path.exists(filepath))
            try:
                with open(filepath, 'r', encoding='utf-8') as desc:
                    print(filepath)
                    data = desc.read()
                    print(data)
                    return data
            except:
                return ''


if __name__ =='__main__':
    read_csv()


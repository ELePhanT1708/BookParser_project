import pandas as pd
from bs4 import BeautifulSoup
import requests

import main
from count_withOut_jpg import search_without_jpg

def find_url(articul):
    with open('../urls_all.txt', 'r') as urls:
        data = urls.readlines()
        for line in data:
            if articul in line:
                return line


def get_lines_withputjpg(path_to_excel):
    data = pd.read_excel(path_to_excel)
    excel = pd.DataFrame(data)
    articuls = excel['Код']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.5060.134 '
                      'Safari/537.36 '
                      'Edg/103.0.1264.77'
    }
    lists = []
    for articul in articuls:

        print(articul)
        url_for_book = find_url(str(articul))
        lists.append(url_for_book[:-2])
        q = requests.get(url_for_book.strip())
        result = q.content
        print(q.status_code)

        print(lists)
        soup = BeautifulSoup(result, 'lxml')
        print(soup.find(data_entity="images-container"))
        try:

            picture = 'https://www.roslit.ru'+soup.find(class_='product-item-detail-slider-images-container').find('img').get('src')
            output = f'Results/{articul}/{articul}.jpg'
            main.download_jpg(picture, output)
            print('Found!!!')
        except:
            pass


if __name__=='__main__':
    get_lines_withputjpg('../Data/Updated.xlsx')
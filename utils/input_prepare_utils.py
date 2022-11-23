import os

import pandas as pd
import requests
from bs4 import BeautifulSoup




def get_url_for_book(id, author, title):
    url_for_search = f'https://www.roslit.ru/catalog/?q={id}&s='
    q = requests.get(url_for_search)
    result = q.content
    soup = BeautifulSoup(result, 'lxml')
    book = soup.find_all(class_='product-item-properties')
    title_soup = soup.find_all(class_='product-item-title')
    length = len(book)
    print(length)
    if length != 1:
        for i in range(length):
            # print(book[i].find('dd').get_text().strip().split('/'))
            array = [i.strip() for i in book[i].find('dd').get_text().strip().split('/')]
            author_current = ', '.join(array)
            # print(author_current)
            # print(author)

            if author_current == author:
                url_for_book = "https://www.roslit.ru" + title_soup[i].find('a').get('href')
                print(url_for_book)
                return url_for_book
    if not title_soup:
        title = title.replace(' ','+')
        title = title.replace(')', '%29')
        title = title.replace('(', '%28')
        url_title = f'https://www.roslit.ru/catalog/?q={title}&s='
        q = requests.get(url_title)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        title_soup = soup.find_all(class_='product-item-title')
    try:
        url_for_book = "https://www.roslit.ru" + title_soup[0].find('a').get('href')
    except:
        url_for_book = '0'
    return url_for_book




def main():
    pass
    path_to = r'D:\Education\Python_Ramil\BookParser_storeland\Data\Позиции_Глобус.xlsx'
    # path_to_2 = r'C:\Users\rkhikmatullin\Desktop\Subjects\Python_practice\BookParser\Data\Позиции_Глобуc_2.xlsx'
    excel_data = pd.read_excel(path_to)
    data = pd.DataFrame(excel_data)
    articular_list = data['Код']
    author_list = data['Автор']
    title_list = data['Наименование']
    for article, author, title in zip(articular_list, author_list, title_list):
        with open('urls_all.txt', 'a') as urls:
            urls.write(get_url_for_book(article, author, title)+'\n')
            print('Good')


if __name__ == '__main__':
    main()

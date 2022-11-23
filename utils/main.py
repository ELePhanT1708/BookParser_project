import requests
from bs4 import BeautifulSoup
import os



def download_jpg(url_for_picture, path_output):
    image_data = requests.get(url_for_picture).content
    with open(path_output, 'wb') as handler:
        handler.write(image_data)

def get_data(url_for_book):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.5060.134 '
                      'Safari/537.36 '
                      'Edg/103.0.1264.77'
    }
    q = requests.get(url_for_book, headers=headers)
    result = q.content
    soup = BeautifulSoup(result, 'lxml')
    title = soup.find(class_="col-lg-9 col-xs-12").get_text().strip() # work
    pictures = ['https://www.roslit.ru'+url.find('img').get('src')
                for url in soup.find_all(class_='product-item-detail-slider-controls-image')] # work
    description = ''
    try:
        description = soup.find(itemprop="description").find('p').get_text()
    except:
        description = 'Описания нет'
    characters = {}
    names = [name.get_text().strip() for name in soup.find_all(class_='product-item-detail-properties__name')]
    values = [value.get_text().strip() for value in soup.find_all(class_='product-item-detail-properties__value')]
    for name, value in zip(names, values):
        characters.update({f'{name}': f'{value}'})
    return title, pictures, description, characters


def main():
    with open('utils/urls_all_1600.txt', 'r') as urls:
        urls_for_book = urls.readlines()
        for line in urls_for_book:
            path_dir = f"Results/{line.split('/')[-2]}"
            os.mkdir(path_dir)
            print(line)
            title, pictures, description, characters = get_data(line.strip())
            print(title)
            print(pictures)
            print(description)
            print(characters)
            with open(os.path.join(path_dir, 'title.txt'), 'w', encoding='utf-8') as txtTitle:
                txtTitle.write(title)
            with open(os.path.join(path_dir, 'description.txt'), 'w', encoding='utf-8') as txtDesc:
                txtDesc.write(description)
            with open(os.path.join(path_dir, 'characters.txt'), 'w', encoding='utf-8') as txtChar:
                txtChar.write(str(characters))
            number = 1
            if not pictures :
                print("Have not picture!")
                pass
            else:
                for picture in pictures:
                    download_jpg(picture.strip(), os.path.join(path_dir, f'{number}.jpg'))
                    number += 1







if __name__ == '__main__':
    main()
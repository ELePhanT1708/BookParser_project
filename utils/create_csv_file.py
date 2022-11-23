import os
import csv, ast

def read_data(src_folder_path):
    header = ['Наименование', 'Артикул', 'Автор', 'Издательство', 'Год издания', 'ISBN', 'Размеры (Д × Ш × В) в см',
              'Предмет', 'Класс', 'Описание', 'Входит в УМК', 'Федеральный перечень', 'Тип материала', 'Учебная система',
              'Группа литературы', 'Количество страниц', 'Тип обложки', 'ФГОС', 'Картинки']
    i = 1
    with open('../data_4.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for dir in os.listdir(src_folder_path):
            title = ''
            articul = dir
            author =''
            Izdatel = ''
            God_izda = ''
            isbn = ''
            Razmer = ''
            Predmet = ''
            clas_s = ''
            description = ''
            umk = ''
            feder_perechen = ''
            type_material = ''
            educat_system = ''
            group_of_liter = ''
            pages = ''
            oblozhka = ''
            fgos = ''

            characters = ''
            pictures = []
            for file in os.listdir(os.path.join(src_folder_path, dir)):
                if 'title' in file:
                    with open(os.path.join(src_folder_path, dir, file), 'r', encoding='utf-8') as f:
                        title = f.read()
                if 'description' in file:
                    with open(os.path.join(src_folder_path, dir, file), 'r', encoding='utf-8') as f:
                        description = f.read()
                if 'characters' in file:
                    with open(os.path.join(src_folder_path, dir, file), 'r', encoding='utf-8') as f:
                        characters = f.read()
                        dict_current = ast.literal_eval(characters)
                        print(dict_current)
                        try:
                            author = dict_current['Автор']
                        except:
                            pass
                        try:
                            Izdatel = dict_current['Издательство']
                        except:
                            pass
                        try:
                            God_izda = dict_current['Год издания']
                        except:
                            pass
                        try:
                            isbn = dict_current['ISBN']
                        except:
                            pass
                        try:
                            Razmer = dict_current['Размеры (Д × Ш × В) в см']
                        except:
                            pass
                        try:
                            Predmet = dict_current['Предмет']
                        except:
                            pass
                        try:
                            clas_s = dict_current['Класс']
                        except:
                            pass
                        try:
                            umk = dict_current['Входит в УМК']
                        except:
                            pass
                        try:
                            feder_perechen = dict_current['Федеральный перечень']
                        except:
                            pass
                        try:
                            type_material = dict_current['Тип материала']
                        except:
                            pass
                        try:
                            educat_system = dict_current['Учебная система']
                        except:
                            pass
                        try:
                            group_of_liter = dict_current['Группа литературы']
                        except:
                            pass
                        try:
                            pages = dict_current['Количество страниц']
                        except:
                            pass
                        try:
                            oblozhka = dict_current['Тип обложки']
                        except:
                            pass
                        try:
                            fgos = dict_current['ФГОС']
                        except:
                            pass
                if '.jpg' in file:
                    pictures.append(os.path.join(src_folder_path, dir, file))
            writer.writerow((title, articul, author, Izdatel, God_izda, isbn, Razmer, Predmet, clas_s, description, umk,
                             feder_perechen, type_material, educat_system, group_of_liter, pages, oblozhka, fgos,
                             pictures))
            print(i)
            i += 1








def main():
    path = '../Results'
    read_data(path)
    pass

if __name__ == '__main__':
    main()

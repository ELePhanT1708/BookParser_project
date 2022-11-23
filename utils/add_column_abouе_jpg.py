from search_similar_pictures import function1
import pandas as pd



def main():
    src_excel = '../Data/Позиции_Глобус.xlsx'
    src_dir = '../Results'
    excel = pd.read_excel(src_excel)
    data = pd.DataFrame(excel)
    list_of_articuls = function1()
    print(list_of_articuls)
    data['Picture'] = [not str(i) in list_of_articuls for i in data['Код']]
    data.to_excel('Data/Updated_2.xlsx')



if __name__ == '__main__':
    main()
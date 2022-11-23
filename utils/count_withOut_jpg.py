import os



def search_without_jpg(path_src):
    list_of_articuls = []
    for root, dirs, files in os.walk(path_src):
        if 'Results\\' in root:
            if True in ['.jpg' in i for i in files]:
                continue
            else:
                list_of_articuls.append(root.split('\\')[1])
    return list_of_articuls



def main():
    path = '../Results'
    array = search_without_jpg(path)
    print(len(array))
    print(array)
    return 1


if __name__ == '__main__':
    # array = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', 'characters.txt', 'description.txt', 'title.txt']
    # if True in ['.jpg' in i for i in array]:
    main()


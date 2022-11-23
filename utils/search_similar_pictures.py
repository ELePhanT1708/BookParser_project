from PIL import Image, ImageChops
import os


def difference_images(img1, img2):
    image_1 = Image.open(img1)
    (wide1, high1) = image_1.size
    image_2 = Image.open(img2)
    (wide2, high2) = image_2.size
    if wide1 == wide2 and high1 == high2:
        print(img1, img2, '\nmatches with size')
        return 1
    return 0



def function1():
    path_to_example = r"C:\Users\rkhikmatullin\Desktop\Subjects\Python_practice\BookParser\Results" \
                      r"\65678555\65678555.jpg"
    quantity = 0
    path_src = "../Results"
    list_of_articuls = []
    for root, dirs, files in os.walk(path_src):
        if 'Results\\' in root:
            if True in ['.jpg' in i for i in files]:
                for file in files:
                    if '.jpg' in file:
                        img1 = path_to_example
                        img2 = os.path.join(root, file)
                        if difference_images(img1, img2):
                            quantity += 1
                            list_of_articuls.append(img2.split('\\')[-1].split('.')[0])

    print(quantity)
    return list_of_articuls


if __name__ == '__main__':
    print(function1())

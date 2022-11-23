import os
import shutil



def main():
    dst_to_path = r'Images'
    if os.path.exists(dst_to_path):
        pass
    else:
        os.mkdir(dst_to_path)
    without_pictures = 0
    for n, dir in enumerate(os.listdir('../Results')):
        src = os.path.join('../Results', dir, '1.jpg')
        dst = os.path.join(dst_to_path, f'{dir}.jpg')
        if os.path.exists(dst):
            print(dst)
        # try:
        #     shutil.copy(src, dst)
        #     print("File was copied !")
        # except:
        #     without_pictures += 1
        #     print(f'Without pictures : {without_pictures}')

    pass


if __name__ =='__main__':
    main()
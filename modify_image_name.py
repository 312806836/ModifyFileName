import os
import shutil

pre_path = "C:/Users/31280/Desktop/诸葛飞1/"
new_path = "C:/Users/31280/Desktop/诸葛飞/"


def get_images():
    path = os.path.abspath(pre_path)
    images = list(os.walk(path))[0][2]
    return images


def modify_name(old_name, new_name):
    shutil.copy(pre_path + old_name, new_path + new_name)


def modify_func():
    images_list = get_images()
    count = 0
    for image in images_list:
        print(image + "   ----    " + str(count) + ".jpg")
        modify_name(image, str(count) + ".jpg")
        if count <= len(images_list):
            count += 1


modify_func()

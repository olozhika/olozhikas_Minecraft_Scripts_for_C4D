# add '.png' to all the files in your folder
# it can be used to extract skins from servers in your \.minecraft\assets\skins

# use it in cmd; IT IS NOT A Cinema4D SCRIPT!
# python rename2png.py yourfolder

import os
import sys

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if not filename.endswith('.png'):
            new_filename = filename + '.png'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('请提供文件夹路径')
        sys.exit(1)

    folder_path = sys.argv[1]

    rename_files(folder_path)
    print('文件名已成功添加 .png 后缀')

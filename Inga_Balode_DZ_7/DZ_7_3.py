import os
from shutil import copy


root_path = '/Users/inga/PycharmProjects/untitled/venv/DZ_7/DZ_7_2/my_project'

for root, dirs, files in os.walk(root_path):
    for file in files:
        if file.split('.')[-1] == 'html':
            file_path = os.path.join(root, file)
            directory = os.path.split(root)[-1]
            temp_path = os.path.join(root_path, 'templates')
            dir_path = os.path.join(temp_path, directory)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            copy(file_path, dir_path)




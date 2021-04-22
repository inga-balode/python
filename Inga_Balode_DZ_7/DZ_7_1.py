import os

main_direct = "my_project"
directories = ['settings', 'mainapp', 'adminapp', 'authapp']


if not os.path.isdir(main_direct):
    os.mkdir(main_direct)

for folder in directories:
    direct_path = os.path.join(main_direct, folder)
    if not os.path.isdir(direct_path):
        os.mkdir(direct_path)


import os

path = '/Users/inga/PycharmProjects/untitled/venv/DZ_7/some_data'
result = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    size = os.stat(file_path).st_size
    if 0 < size < 100:
        result[100] += 1
    elif 100 <= size < 1000:
        result[1000] += 1
    elif 1000 <= size < 10000:
        result[10000] += 1
    elif 10000 <= size < 100000:
        result[100000] += 1

print(result)
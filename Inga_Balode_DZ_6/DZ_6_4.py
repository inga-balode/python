# 4. Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:

result_list = []
with open('users.csv', encoding='utf-8') as f1, open('hobby.csv', encoding='utf-8') as f2:
    users = f1.readline().strip()
    hobby = f2.readline().strip()
    while users:
        user_list = users.split(',')
        user_name = ' '.join(user_list)
        result = f'{user_name} : {hobby} \n'
        result_list.append(result)
        users = f1.readline().strip()
        hobby = f2.readline().strip()

print(result_list)

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    f.writelines(result_list)

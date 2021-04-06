
#!/usr/bin/python
# -*- coding: utf- 8 -*-

import csv
import pickle

with open('users.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']])

with open('hobby.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['скалолазание', 'охота'], ['горные лыжи']])

result = {}
with open('users.csv', encoding='utf-8') as f1, open('hobby.csv', encoding='utf-8') as f2:
    users = f1.readline().strip()
    hobby = f2.readline().strip()
    while users:
        result[users] = hobby
        users = f1.readline().strip()
        hobby = f2.readline().strip()
print(result)

with open('result.pickle', 'wb') as f:
    pickle.dump(result, f)




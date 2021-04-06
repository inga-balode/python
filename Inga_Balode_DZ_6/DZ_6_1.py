# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        info = line.split(' ')
        remote_addr = info[0]
        request_type = info[5][1:]
        requested_resource = info[6]
        result = (remote_addr, request_type, requested_resource)
        print(result)



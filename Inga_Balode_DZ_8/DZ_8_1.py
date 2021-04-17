import re

def email_parse(email_address):
    pattern = r'[\w\.-]+@[\w\.-]+(\.[\w]+)+'
    compiled_pattern = re.compile(pattern)
    if compiled_pattern.fullmatch(email_address) == None:
        raise ValueError
    else:
        result = email_address.split('@')
        result_dict = {'username': result[0], 'domain': result[1]}
        return result_dict

print(email_parse('someone@geekbrains.ru'))
from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
personalities = {}
for contact in contacts_list:
    fio = ' '.join(contact[:2]).strip().split(' ')
    contact = fio + contact[len(fio):]

    pattern = r'(8|\+7)[\s\(]*(\d{3})[\s\)-]*(\d{3})-?(\d{2})-?(\d{2})[\s\(]*(доб\.)*\s*(\d{4})*[\s\)]*'
    contact[5] = re.sub(pattern, r'+7(\2)\3-\4-\5 \6\7', contact[5]).strip()

    contact_id = ' '.join(contact[:2])
    if not contact_id in personalities.keys():
        personalities[contact_id] = contact
    else:
        for i in range(5):
            if len(personalities[contact_id][2+i].strip()) == 0:
                personalities[contact_id][2+i] = contact[2+i]

contacts_list = list(personalities.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)


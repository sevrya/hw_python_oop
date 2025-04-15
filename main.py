import datetime as dt

date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('16.04.2025', date_format).date()
print(moment)

now = dt.datetime.now().date()
print(now)

print(moment > now)

date = dt.datetime.now().strftime('%d.%m.%Y')
print(date)

my_list = [1, 2, 3]

# Создаем словарь
my_dict = {'a': 1, 'b': 2}

# Добавляем словарь в список
my_list.append(my_dict)

print(my_list)

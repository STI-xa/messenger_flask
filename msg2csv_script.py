import csv

header = ['Автор', 'Текст', 'Дата сообщения']

data = [
    ['Петя', 'Привет, мир!', '01.01.2022'],
    ['Даша', 'Как дела?', '02.01.2022'],
    ['Оля', 'Что нового?', '03.01.2022']
]

with open('messages.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)

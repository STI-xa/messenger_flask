import json

data = [
    {'author': 'Петя', 'text': 'Привет, мир!', 'date': '2021-10-01'},
    {'author': 'Даша', 'text': 'Как дела', 'date': '2021-10-02'},
    {'author': 'Оля', 'text': 'Что нового?', 'date': '2021-10-03'}
]

with open('msg.json', 'w') as outfile:
    json.dump(data, outfile)

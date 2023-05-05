import json

with open('msg.json', 'r') as infile:
    data = json.load(infile)

for message in data:
    print('Author:', message['author'])
    print('Text:', message['text'])
    print('Date:', message['date'])
    print('-------------------')

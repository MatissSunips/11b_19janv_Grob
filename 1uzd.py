import json

with open('1uzd.json', 'r', encoding='utf8') as sk:
    info=json.load(sk)

print(info["datorspeles"])
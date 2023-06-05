import json
from json_combine.checker import anses1

# print(anses1)

with open('test_intermed.json','w',encoding='utf-8') as file:
    json.dump(anses1,file)



import json
from typing import Union

def write_json(data:Union[dict, list], file_loc:str):
    with open(file_loc, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f'data saved to: {file_loc}')

def read_json(file_loc:str):
    with open(file_loc, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
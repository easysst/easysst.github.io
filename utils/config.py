import json

def get_config(name:str):
    with open(f'./configs/{name}.json') as f:
        config = json.load(f)
    return config
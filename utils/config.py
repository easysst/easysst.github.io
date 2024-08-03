import json

def getConfig(name:str):
    with open(f'./configs/{name}.json') as f:
        config = json.load(f)
    return config
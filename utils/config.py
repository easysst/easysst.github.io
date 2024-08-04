import json

def get_config(name:str):
    with open(f'./configs/{name}.json') as f:
        config = json.load(f)
    return config

def save_config(name:str, config):
    with open(f'./configs/{name}.json', 'w') as f:
        json.dump(config, f)
    return config
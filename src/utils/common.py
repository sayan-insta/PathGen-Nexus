import yaml

def read_yaml(path):

    with open(path) as file:

        return yaml.safe_load(file)
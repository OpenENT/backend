import json

class Settings:

    def __init__(self, path):
        self.path = path
        self.local_provider_path = './music'
        try:
            with open(self.path) as f:
                self.__dict__.update(json.load(f))
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.__dict__, f, indent=4, sort_keys=True)

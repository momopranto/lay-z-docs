# lay-z-docs package object

class Package:
    def __init__(self):
        self.language = None
        self.data = None

    def __init__(self,lang, json_data):
        self.language = lang
        self.data = json_data

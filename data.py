import json
import os

class UserData:
    def __init__(self):
        if not os.path.isfile("data.json"):
            with open("data.json", "w") as data_file:
                data_file.write("{}")
        
        self.load()

    
    def load(self):
        with open("data.json", "r") as data_file:
            self.data = json.load(data_file)


    def save(self):
        with open("data.json", "w") as data_file:
            json.dump(self.data, data_file)
    

    def get_inv(self, user):
        inv = self.data[user]["inventory"]
        if inv:
            return ", ".join(inv)
        else:
            return "(empty)"


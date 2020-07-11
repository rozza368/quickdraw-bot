import json
import os

class UserData:
    def __init__(self):
        if not os.path.isfile("data.json"):
            with open("data.json", "w") as data_file:
                data_file.write("{}")
        
        with open("default_data.json", "r") as default:
            self.default_data = json.load(default)

        self.load()

    
    def load(self):
        with open("data.json", "r") as data_file:
            self.data = json.load(data_file)


    def save(self):
        with open("data.json", "w") as data_file:
            json.dump(self.data, data_file, indent=4)
    

    def get_inv(self, user):
        inv = self.data.get(user).get("inventory")
        if inv:
            return ", ".join(inv)
        else:
            return "(empty)"
    

    def get_value(self, user, key):
        return self.data[user].get(key)
    

    def is_usr(self, user):
        return bool(self.data.get(user))


    def init_usr(self, user):
        self.data[user] = self.default_data
        self.save()


if __name__ == "__main__":
    ud = UserData()
    print(ud.is_usr("asdf"))
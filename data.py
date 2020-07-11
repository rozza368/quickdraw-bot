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
        if self.is_usr(user):
            self.check_usr(user)
            inv = self.data.get(user).get("inventory")
            if inv:
                return "'s inventory:\n, ".join(inv)
            else:
                return "'s inventory:\n(empty)"
        else:
            return ":\nUser hasn't registered"

    

    def get_value(self, user, key):
        self.check_usr(user)
        return self.data[user].get(key)
    

    def set_value(self, user, key, value):
        self.check_usr(user)
        self.data[user][key] = value
    

    def set_profile(self, user, key, value):
        self.check_usr(user)
        self.data[user]["profile"][key] = value
    

    def has_profile(self, user):
        self.check_usr(user)
        # true if the name is filled out
        return self.data[user]["profile"]["name"]
    

    def is_usr(self, user):
        return bool(self.data.get(user))


    def check_usr(self, user):
        if not self.is_usr(user):
            self.data[user] = self.default_data
            self.save()


if __name__ == "__main__":
    # testing
    ud = UserData()
    print(ud.is_usr("asdf"))
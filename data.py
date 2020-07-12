import json
import os

class UserData:
    def __init__(self):
        if not os.path.isfile("data.json"):
            with open("data.json", "w") as data_file:
                data_file.write("{}")
        
        with open("default_data.json", "r") as default:
            self.default_data = json.load(default)

        with open("data.json", "r") as data:
            self.data = json.load(data)


    def save(self):
        with open("data.json", "w") as data_file:
            json.dump(self.data, data_file, indent=4)
    
# This part is good
    def get_inv(self, user, admin):
        if self.is_user(user):
            self.create_id(user)
            inv = self.data.get(user).get("inventory")
            if inv:
                return "'s inventory:\n, ".join(inv)
            else:
                return "'s inventory:\n(empty)"
        else:
            if admin:
                return ":\nUser hasn't registered"
            else:
                return ":\nYou haven't registered"


    def get_value(self, user, key):
        self.create_id(user)
        return self.data[user].get(key)
    

    def set_value(self, user, key, value):
        self.create_id(user)
        self.data[user][key] = value
    

    def set_profile(self, user, key, value):
        self.data[user]["profile"][key] = value
    

    def has_profile(self, user):
        self.is_user(user)
        # true if the name is filled out
        return self.data[user]["profile"]["name"]
    

    def is_user(self, user):
        return bool(self.data.get(user))


    def create_id(self, user):
        if not self.is_user(user):
            self.data[user] = self.default_data
            self.save()
            return ', \nEntering character setup:'
        else:
            return ", \nYou already have registered."


if __name__ == "__main__":
    # testing
    ud = UserData()
    print(ud.is_user("asdf"))
from User import User


class Privileges:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(self.first_name + " " + self.last_name + " " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, **other_info):
        super().__init__(first_name, last_name, **other_info)
        self.privileges = Privileges(self.first_name, self.last_name)

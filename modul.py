User = {
    "name": "Akbar",
    "username": "@akbar",
    "password": "@akbar09",
    "email": "akbarb@gmail.com",
}


class Users:
    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password


users = Users("Akbar", "@akbar", "@akbar3475", "akabar@gmail.com")

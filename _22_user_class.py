class User:
    def __init__(self, username, email, password):
        self.username = username
        self.emai = email
        self.password = password

class Admin(User):
    def __init__(self, username, email, password, role='Admin'):
        super().__init__(username, email, password)
        self.role = role
        self.users = []

    def create_user(self, username, email, password):
        self.email = email
        self.password = password
        if username in self.users:
            print(f"The username '{username}' already exists.")

        else:
            self.users.append(username)
            print(f"The user '{username}' has successfully created an account.")

    def delete_user(self, username):
        if username in self.users:
            self.users.remove(username)
            print(f"The account for user '{username}' has been deleted.")

        else:
            print(f"Cannot delete account for '{username}' because it does not exist.")

    def display_user_info(self):
        print('-'*60)
        print(f"User Name: {self.username}\nEmail: {self.email}\nPassword: {self.password}")



admin1 = Admin("", "", "")
admin1.create_user('Aang', 'aang1234@gmail.com', 't2t2')

admin2 = Admin("", "", "")
admin2.create_user('John', 'john8764@gmail.com', 'y3y2')

# admin.delete_user('Aang')
admin1.delete_user('Peter')

admin1.display_user_info()
admin2.display_user_info()


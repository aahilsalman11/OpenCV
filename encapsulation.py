class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        admin_password = input("Enter admin password to access user password: ")
        if admin_password == "admin123":
            return self.__password
        else:
            return "Access denied. Incorrect admin password."
        
user1 = User("john_doe", "securepassword123")
print(user1.username)
answer = user1.get_password()
print(answer)

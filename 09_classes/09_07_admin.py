# Using the previous User Class 
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
    
    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"\n\tHello, {self.first_name}. Welcome back!")

# Create class called Admin that inherits from the User class
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify user privileges"
        ]

    def show_privileges(self):
        print(f"\nAdmin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Creating an instance of Admin
admin1 = Admin("Alice", "Smith", 30, "San Francisco", "alice@gmail.com")

# Calling methods for the admin
admin1.describe_user()
print()  
admin1.greet_user()
print()  
admin1.show_privileges()
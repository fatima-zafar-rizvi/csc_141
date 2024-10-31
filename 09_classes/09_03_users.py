# Creating User Class
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
    
    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name:{self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"\n\tHello, {self.first_name}. Welcome back!")

# Creating several instances of the user class
user1 = User("Maya", "Hunter", "hunt@yahoo.com", 22, "New York")
user2 = User("Joshua", "Matthews", "boing@yahoo.com", 25, "Los Angeles")
user3 = User("Charlie", "Gardener", "charlie@gmail.com", 35, "Chicago")

# Calling methods for each user
users = [user1, user2, user3]

for user in users:
    user.describe_user()
    print()  
    user.greet_user()
    print()  
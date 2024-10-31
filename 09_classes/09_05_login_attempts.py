# Using the previous User Class 
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0 # Initialize login_attempts
    
    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name:{self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"\n\tHello, {self.first_name}. Welcome back!")
    
    def increment_login_attempts(self):
        '''Increment login attempts by 1.'''
        self.login_attempts +=1

    def reset_login_attempts(self):
        '''Reset the number of login attempts back to 0.'''
        self.login_attempts = 0

# Creating several instances of the user class
user = User("Maya", "Hunter", "hunt@yahoo.com", 22, "New York")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the current number of login attempts
print(f"\nLogin attempts: {user.login_attempts}")

# Reset login attempts and print the value again
user.reset_login_attempts()
print(f"\nLogin attempts after reset: {user.login_attempts}\n")
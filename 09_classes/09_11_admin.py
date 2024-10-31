# Import from user_management.py
from user_management import Admin

# Create an instance of Admin
admin1 = Admin("Alice", "Smith", 30, "San Francisco", "alice@gmail.com")

# Call methods to demonstrate that everything is working correctly
admin1.describe_user()
print()  
admin1.greet_user()
print()  
admin1.privileges.show_privileges()  
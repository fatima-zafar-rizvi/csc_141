# Import admin_privileges.py which also has user.py in it
from admin_privileges import Admin

# Create an instance of Admin
admin1 = Admin("Alice", "Smith", 30, "San Francisco", "alice@gmail.com")

# Call methods to check that everything is still working correctly
admin1.describe_user()
print()  
admin1.greet_user()
print()  
admin1.privileges.show_privileges()  
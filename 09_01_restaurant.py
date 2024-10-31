# Creating Restaurant Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize the restaurant name and what cuisine it offers.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"\nCuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!\n")

# Creating an instance of the Restaurant Class
restaurant = Restaurant('Olive Garden', 'Italian')

# Printing attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling on both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
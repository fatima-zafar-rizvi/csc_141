# Using the previous Restaurant Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!\n")

    def set_number_served(self, number):
        '''Set the number of customers served.'''
        self.number_served = number

    def increment_number_served(self, number):
        '''Increment the number of customers served by a specified amount.'''
        self.number_served += number

# Creating an instance of the Restaurant class
restaurant = Restaurant('Olive Garden', 'Italian')

# Calling on both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Print the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Change the number served and print it again
restaurant.set_number_served(50)
print(f"Number of customers served after setting: {restaurant.number_served}")

# Increment the number served and print it
restaurant.increment_number_served(20)  # 20 more customers were served.
print(f"Number of customers served after incrementing: "
      f"{restaurant.number_served}")

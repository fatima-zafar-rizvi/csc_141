# Restaurant Class from Exercise 09_01:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating three different instances of the Restaurant class
restaurant1 = Restaurant("Ratatouille's Kitchen", "French")
restaurant2 = Restaurant("Taj Mahal", "Indian")
restaurant3 = Restaurant("Vincenzo", "Italian")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
print()  
restaurant2.describe_restaurant()
print()  
restaurant3.describe_restaurant()
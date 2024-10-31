class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize the restaurant name and what cuisine it offers.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!\n")

# Creating class called IceCreamStand which inherits from Restaurant class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize the IceCreamStand, inheriting from Restaurant.'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # Initialize an empty list of flavors

    def add_flavor(self, flavor):
        '''Add a flavor to the list of flavors.'''
        self.flavors.append(flavor)

    def display_flavors(self):
        '''Display the list of ice cream flavors.'''
        print(f"Available ice cream flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Creating an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand('Primo Cafe Gelato', 'Dessert')

# Adding flavors to the ice cream stand
ice_cream_stand.add_flavor('French Vanilla')
ice_cream_stand.add_flavor('Chocolate Chip Cookie')
ice_cream_stand.add_flavor('Strawberry Cheesecake')

# Calling methods to display the ice cream stand details and flavors
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()
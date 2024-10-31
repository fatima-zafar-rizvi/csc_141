# Final version of electric_car.py from the book
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """Attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"This car can go about {range_miles} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrade the battery size to 65 kWh if it isn't already."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at 65 kWh.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


# Create an electric car with a default battery size
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Display the car's description and initial battery information
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# Upgrade the battery and check the range again
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
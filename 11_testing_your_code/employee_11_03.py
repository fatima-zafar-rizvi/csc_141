# Make a class to represent an employee.
class Employee:
    
    def __init__(self, first_name, last_name, annual_salary):
        # Initializing the attributes.
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        # Add the raise to the annual salary, default to $5,000.
        self.annual_salary += amount
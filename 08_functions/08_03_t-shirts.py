
def make_shirt(size, message):
    print(f"\nThe size of this shirt is {size} and its has {message} printed "
          "on it.")
    
# Calling the function with positional arguments:
make_shirt("Small", "Python Power!")

# Calling the function with keyword arguments:
make_shirt(size="Medium", message="Hello World!")
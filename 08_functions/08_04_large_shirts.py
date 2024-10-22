
def make_shirt(size="Large", message="I love Python"):
    print(f"\nThe size of this shirt is {size} and it has {message}"
          " printed on it.")

# Calling the function with the default size and message:
make_shirt()

# Calling the function with a medium shirt using the default message:
make_shirt(size="Medium")

# Calling the function with a different message:
make_shirt(size="Small", message="Code is Life!")

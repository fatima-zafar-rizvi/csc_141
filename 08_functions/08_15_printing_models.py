
# printing_models.py

import printing_functions


from printing_functions import print_models, show_completed_models

# List of designs to print
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Print the models
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

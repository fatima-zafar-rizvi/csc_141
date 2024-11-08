# Challenge level 6/10
def read_pet_names(file_name):
    try:
        with open(file_name, 'r') as file:
            pet_names = file.readlines()
            print(f"\n\tContents of {file_name}:")
            if pet_names:
                for name in pet_names:
                    print(name.strip())  
            else:
                print(f"The file {file_name} is empty.")
    except FileNotFoundError:
        pass  # Fails silently if the file is missing.

# Attempt to read both files
read_pet_names('cats.txt')
read_pet_names('dogs.txt')
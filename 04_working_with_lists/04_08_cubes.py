# Making list of cubes of each integer from 1-10.
# Then using for loop to print it.
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

print(cubes)
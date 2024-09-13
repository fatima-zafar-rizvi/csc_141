
# Program from Exercise 03_06:
guests = ['Mansour', 'Sumin', 'Willfredo', 'Abi']

print ("Hey guys, we have more room on the guest list as I just found a bigger table.")

guests.insert(0, 'Dave')

guests.insert(3, 'Bob')

guests.append('Michael')

print("\nDear "+ guests[0] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[1] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[2] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[3] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[4] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[5] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

print("\nDear "+ guests[6] +", I would like to invite you to dinner at Roessner Hall in Room 101 tomorrow.")

# Program for Exercise 03_07:
print("\nHey guys, I have some bad news. I can only invite two people for dinner as my new dinner table is not able to get here on time.")

# Using pop method to shrink the guest list:
print(guests)

popped_guests = guests.pop()

print("\nSorry " + popped_guests + ", you are uninvited.")

popped_guests = guests.pop()

print("\nSorry " + popped_guests + ", you are uninvited.")

popped_guests = guests.pop()

print("\nSorry " + popped_guests + ", you are uninvited.")

popped_guests = guests.pop()

print("\nSorry " + popped_guests + ", you are uninvited.")

popped_guests = guests.pop()

print("\nSorry " + popped_guests + ", you are uninvited.")

# Letting the last two people know that they are still invited.
print(guests)

print("\nDear "+ guests[0] +", you are still invited for dinner tomorrow.")

print("\nDear "+ guests[1] +", you are still invited for dinner tomorrow.\n")

del guests[0]
del guests[0]
print(guests)

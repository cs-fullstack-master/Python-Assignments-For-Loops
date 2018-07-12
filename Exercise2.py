import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("\n")

# Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20
for kount in range(0, 21, 2):
    print(kount)

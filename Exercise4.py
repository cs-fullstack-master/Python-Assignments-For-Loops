import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("\n")

# Exercise 4: Use any loop to print all numbers between 0 and 100 that's a multiple of 4. Hint: You can find
# multiples of 4 with (number % 4 == 0)
for kount in range(0, 101, 4):
    if kount != 0:
        print(kount)

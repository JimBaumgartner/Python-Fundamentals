puzzle = open('frequencies.txt', 'r').read().split("\n") # "\n" means new line
numbers = [int(i) for i in puzzle]

# what is ther final frequency

# #this challenge is to find out the final location of the person,
# starts at 0,  then -18, +4 etc ( these numbers are in the txt functions)
final_step = 0

for each_item in numbers:
    final_step += each_item

print(final_step)

## to do the same thing with while loop see below
x = 0
total = 0

while x < len(numbers):
    total += numbers[x]
    x += 1

print(total)


built_in = sum(numbers)

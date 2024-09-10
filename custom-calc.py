# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

print('Hello. This calculator is a pyramid calculator. ')

units = input('Enter the units you want to use. E.g. cm, m, ft, etc. : ')
length = float(input('Please enter the length: '))
#print(type(length))
width = float(input('Please enter the width: '))
#print(type(width))
height = float(input('Please enter the height: '))
#print(type(height))


total = int(length * width * height) / 3
print(f'Your pyramid is {total} cubic {units}!')



# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!





# Using 'elif' Statement
print("1. Using 'elif' Statement")

# Example 1: Determine grade based on score
print("Example 1: Determine Grade Based on Score")
score = 85
if score >= 90:
    print("You got an A.")  # This will not be printed
elif score >= 80:
    print("You got a B.")  # This will be printed
elif score >= 70:
    print("You got a C.")  # This will not be printed
else:
    print("You got a D or lower.")
print()  # Blank line for spacing

# Example 2: Check the day of the week
print("Example 2: Check the Day of the Week")
day = "Wednesday"
if day == "Monday":
    print("It's the start of the week.")  # This will not be printed
elif day == "Wednesday":
    print("It's the middle of the week.")  # This will be printed
elif day == "Friday":
    print("It's almost the weekend.")  # This will not be printed
else:
    print("It's another day.")
print()  # Blank line for spacing

# Example 3: Determine the type of triangle based on angles
print("Example 3: Determine the Type of Triangle Based on Angles")
angle1 = 60
angle2 = 60
angle3 = 60

if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("It's a right triangle.")  # This will not be printed
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("It's an obtuse triangle.")  # This will not be printed
else:
    print("It's an acute triangle.")  # This will be printed
print()  # Blank line for spacing

# Example 4: Check temperature category
print("Example 4: Check Temperature Category")
temperature = 30  # in Celsius
if temperature < 0:
    print("It's freezing!")  # This will not be printed
elif temperature < 20:
    print("It's cold.")  # This will not be printed
elif temperature < 30:
    print("It's warm.")  # This will be printed
else:
    print("It's hot!")
print()  # Blank line for spacing

# Example 5: Check age group
print("Example 5: Check Age Group")
age = 15
if age < 13:
    print("You are a child.")  # This will not be printed
elif age < 20:
    print("You are a teenager.")  # This will be printed
elif age < 65:
    print("You are an adult.")  # This will not be printed
else:
    print("You are a senior.")
print()  # Blank line for spacing

# Example 6: Determine if a number is positive, negative, or zero
print("Example 6: Determine If a Number Is Positive, Negative, or Zero")
number = -10
if number > 0:
    print("The number is positive.")  # This will not be printed
elif number < 0:
    print("The number is negative.")  # This will be printed
else:
    print("The number is zero.")
print()  # Blank line for spacing


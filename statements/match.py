# Using 'match' Statement
print("Using 'match' Statement")

# Example 1: Determine if the day is a weekday or weekend
print("Example 1: Determine if the Day is a Weekday or Weekend")
day = "Wednesday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday.")  # This will be printed
    case "Saturday" | "Sunday":
        print("It's the weekend.")
    case _:
        print("Invalid day.")
print()  # Blank line for spacing


# Example 2: Traffic light color action
print("Example 2: Traffic Light Color Action")
light_color = "Yellow"
match light_color:
    case "Red":
        print("Stop.")  # This will not be printed
    case "Yellow":
        print("Slow down.")  # This will be printed
    case "Green":
        print("Go.")
    case _:
        print("Invalid color.")
print()  # Blank line for spacing


# Example 3: Match number with ranges
print("Example 3: Match Number with Ranges")
number = 75
match number:
    case n if 0 <= n < 50:
        print("The number is between 0 and 49.")  # This will not be printed
    case n if 50 <= n < 100:
        print("The number is between 50 and 99.")  # This will be printed
    case _:
        print("The number is 100 or greater.")
print()  # Blank line for spacing


# Example 4: Determine pet type based on species
print("Example 4: Determine Pet Type Based on Species")
pet = "Dog"
match pet:
    case "Cat":
        print("You have a cat.")  # This will not be printed
    case "Dog":
        print("You have a dog.")  # This will be printed
    case "Bird":
        print("You have a bird.")
    case _:
        print("Unknown pet type.")
print()  # Blank line for spacing


# Example 5: Match multiple conditions
print("Example 5: Match Multiple Conditions")
fruit = "Apple"
match fruit:
    case "Apple" | "Banana" | "Mango":
        print("It's a common fruit.")  # This will be printed
    case "Dragonfruit" | "Durian":
        print("It's an exotic fruit.")
    case _:
        print("Unknown fruit.")
print()  # Blank line for spacing

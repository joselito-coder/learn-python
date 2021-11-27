# Problem Statement:-

# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:

#     Do not use any type of module like DateTime or date utils. (-5 points)
#     Users can optionally provide a year, and your program must tell their age in that particular year. (3points)

#     Your code should handle all sorts of errors like :            (2 points)
#     You are not yet born
#     You seem to be the oldest person alive
#     You can also handle any other errors, if possible!

# Problem Solution:

def take_optional_year():
    optional_year = input("\nDo you want to Enter a year? (y/n) ")

    if optional_year.lower() == "y":
        user_year = int(input("Enter year: "))
        if not is_year(user_year):
            return
        return user_year
    elif optional_year.lower() == "n":
        return
    else:
        take_optional_year()

def is_age(num):
    if num < 150 and len(str(num)) < 3:
        return True
    else:
        return False

def is_year(year):
    if len(str(year)) == 4:
        return True
    else:
        return False
    

def handle_age_or_year(age_or_year):
    # Take optional year
    optional_year = take_optional_year()

    if is_age(age_or_year):
        # If the above condition is true then it's a age

        birth_year = current_year - age_or_year
        # Check if the user has been born 
        if birth_year >= current_year:
            print("You are not yet born")
            exit()

        # Calculate when the user will be 100 years
        years_100 = birth_year + 100
        print(f"You will turn 100 in {years_100}")
        # Handle if the user has entered optional year
        if optional_year != None:
            age_optional_year = optional_year - birth_year
            if not age_optional_year < 0:
                print(f"You will turn {age_optional_year} in {optional_year}")

    # If the user input is a year then handle year 
    elif is_year(age_or_year):
        if age_or_year >= current_year:
            print("You are not yet born")
            exit()
        # Calculate when the user will turn 100 years
        years_100 = age_or_year + 100
        print(f"You will turn 100 in {years_100}")
        # Handle if the user has entered optional year
        if optional_year != None:
            age_optional_year = optional_year - age_or_year
            if not age_optional_year < 0:
                print(f"You will turn {age_optional_year} in {optional_year}")
    else:
        print("Invalid Age or year")
        exit()

# Store the current year
current_year = 2021
try:
    age_or_year = int(input("Enter age or year: "))

    handle_age_or_year(age_or_year)
#  Handle if the user has entered an invalid year like "asdf" 
except ValueError:
    print("Please enter a valid age or year")
    exit()


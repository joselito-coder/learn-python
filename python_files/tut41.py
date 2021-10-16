# def function_print_name(a,b,c,d,e):
#     print(a,b,c,d,e)

# function_print_name("Harry", "Rohan", "Skillf", "Hammad","Shivam")

def funargs(babu, *args, **kwargs):
    print(f"The babu is {babu}")
    for item in args:
        print(item)

    print("\nNow I would like to introduce you to some of the important people")
    for key, value in kwargs.items():
        print(f"{key} is {value}")


har = ["Harry", "Rohan", "Skillf", "Hammad","Shivam", "the programmer"]

kwargs = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
          "The Programmer": "Coordinator", "Shivam": "Cook"}

funargs("melfern",*har, **kwargs)

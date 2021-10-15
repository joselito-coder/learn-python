import random

# random_number = random.randint(0, 10)
# print(random_number)
# rand = random.random()
# print(rand)

# lst = ["Python","Javascript","Java","C","Php","CodeWithHarry"]
# choice = random.choice(lst)
# print(choice)

# Task : pick any two modules and use 2 functions from it 

# # Module 1 ==> webbrowser 
# # webbrowser let's us open webpages inside our default browser
# # importing webbrowser
# import webbrowser
# url = "https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME"

# # we use the open function of the webbrowser module to open websites
# webbrowser.open(url)

# # If we wanted to open the webpage in new window we can use the  open_new function
# webbrowser.open_new(url)

# Module 2 ==> pyperclip
# pyperclip lets you manipulate clipboard, for eg. We can copy text from variable to our clipboard
# to install pyperclip first type pip install pyperclip

# importing pyperclip
import pyperclip

# copying text to the clipboard
text = "CodeWithHarry is the best channel"
pyperclip.copy(text)

# We can Also get the contents of the clipboard and store it inside a variable
clip_text = pyperclip.paste()
# should print CodeWithHarry is the best channel
print(clip_text)


import webbrowser

class Dio:
    def __init__(self,name='Dio'):
        self.name = name

    def print_name(self):
        print(f"Kono {self.name} da!!!")

    @staticmethod
    def watch_video():
        # Opens kono dio da inside the default browser
        webbrowser.open('https://www.youtube.com/watch?v=HaGkk60kcjQ')
        

# Quiz solution
# Readme.txt ==> README files can help your users understand your project and can be used to set your project’s description on PyPI ( the official third-party software repository for Python). It also contains information about what the project does and how to use it

# license.txt ==> a license tells users who install your package the terms under which they can use your package. There are many types of license: some are more permissive and some are less permissive
# More permissive:
#    PSFL (Python Software Foundation License)
#    MIT / BSD / ISC
#    Apache
# Less permissive:
#    LGPL
#    GPL
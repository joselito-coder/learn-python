import re

# String
string = """ hallo phrands chai pilo asdf asdf asdf asdf;kasjd;lk asdf;lkjas d;flkjasd;fl asdf
rice.dangelo@carter.com
emely58@durgan.com arlie61@gmail.com some random jibberish
estrella.kris@reilly.com
This site is offered as is to those who visit it. We make no guarantees regarding its services. Just enjoy yourself.
pp##pupu@bmail.com
hahahahahahahahahahahah some random jibberish that you won't understand asd;lkfjas; dlfkj;asldkj;laksjdf;lkajsdfl;kja;sdlfkja;sldfjka;lsdkfj;laskdfjal;ksdjf;laksdf
"""

# regex for extracting emails
email_regex = re.compile(r'[A-Za-z.0-9_-]+@[A-Za-z.0-9]+\.[A-Za-z.0-9]{2,8}')

# store the email matches
email_matches  = email_regex.findall(string)

# Only open a file for writing if there are matches else print no matches
if len(email_matches) !=0:
    with open("emails.txt",'w') as email_file:

        for index,email in enumerate(email_matches):
            email_file.write(f"Email {index + 1}\t{email}\n")
    print("wrote all found emails into file named emails.txt")
else:
    print("No matches found")
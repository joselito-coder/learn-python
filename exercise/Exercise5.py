# Health Management System
# 3 clients - Harry, Rohan and Hammad
#  Total 6 files 
# Write a function that when executed takes as input client name

# Store corresponding file locations 
client_dict = {
    "Harry": "ex5_txt_files/Harry_",
    "Rohan": "ex5_txt_files/Rohan_",
    "Hammad": "ex5_txt_files/Hammad_"
}

log_dict = {
    "exercise" : "exercise.txt",
    "diet" : "diet.txt"
}

def getClient(log_or_read):
    # Prompt the user to enter input
    print("Which client do you want to " +log_or_read+"?\nYour Options are:")
    print("1.Harry\n2.Rohan\n3.Hammad")
    try:
        client_number  = int(input(">> "))
    except Exception as e:
        print("Invalid")
    
    # Take a valid input from the user
    while( client_number > 3):
        try:
            print("Please try again with correct Number: ")
            client_number  = int(input(">> "))
        except Exception as e:
            print("Invalid")
    
    # return the name based on the valuet entered
    if client_number == 1:
        return "Harry"
    elif client_number == 2:
        return "Rohan"
    elif client_number == 3:
        return "Hammad"


def getClientType(log_or_read):
    print("What do you want to "+log_or_read+"?\nYour Options are:")
    print("1.Exercise\n2.Diet")
    # check if the user enters something invalid 
    try:
        client_type  = int(input(">> "))
    except Exception as e:
        print("Invalid")

    # Return value based on the number entered by the user
    if client_type == 1:
        return "exercise"
    elif client_type == 2:
        return "diet"
    else: return ""

def readFile(name,e_or_d):
    # print(name+e_or_d)
    try:
        with open(name+e_or_d) as f:
            print()
            print(f.read())
    except :
        print("Sorry That data isn't available\nPlease log more data first")


# function to log to a file
def logFile(name,typeOfH):
    print("Enter values: ")
    with open(name+typeOfH,"a") as f:
        # Write for the first time
        user_inp = input(">> ")
        if user_inp != "":
            f.write("["+str(getdate())+"] " +  user_inp + "\n")
        
        # ask if the user wants to enter more
        enter_more = input("Do you want to enter more?(y/n)\n>> ")
        # if the user's answer is yes then log until he inputs exit
        if enter_more.startswith('y'):
            print("Press exit to stop")
            while(1):
                user_inp = input(">> ")
                if(user_inp == "exit"):
                    print("Logged successfully")
                    break
                else:
                    if user_inp != "":
                        f.write("["+str(getdate())+"] " +  user_inp + "\n")
        else:
            print("Successfully logged")

def getLogRead():
    print("What do you want to do: ")
    print("1.log\n2.read")

    try:
        user_inp  = int(input(">> "))
    except Exception as e:
        print("Invalid")

    if( user_inp == 1):
        return "log"
    elif (user_inp == 2 ):
        return "read"


def getdate():
    import datetime
    return datetime.datetime.now()

log_or_read = getLogRead()
client = getClient(log_or_read)
client_type = getClientType(log_or_read)

if client in client_dict and client_type in log_dict:
    if log_or_read == "log":
        logFile(client_dict.get(client), log_dict.get(client_type))
    else:
        readFile(client_dict.get(client), log_dict.get(client_type))
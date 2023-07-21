import os
# add users here
userCredential = {"payal": "payal123", "harry": "harry007", "joe": "joe123"}
numberOfUserLoggedinn = 0
alreadyLoggedin = {}
while True:
    option = int(input('''Enter => 
1 for login.
2 for logout.
3 to display name and number of logged in user.
4 to exit.
=>  '''))
    os.system('cls')
    match option:
        case 1:
            print("INITIATE LOGIN.")
            # getting individual keys and values from the userCredential
            username = userCredential.keys()
            password = userCredential.values()
            # login process
            inpusername = input("Enter your User Name: ")
            inppassword = input("Enter your Password: ")
            os.system('cls')
            # Credential check
            if inpusername in username and inppassword in password and inpusername not in alreadyLoggedin:
                print("Login Successful")
                # adding user to alreadyLoggedin list
                alreadyLoggedin.update({inpusername: inppassword})
                numberOfUserLoggedinn += 1
            elif inpusername in alreadyLoggedin and inppassword in alreadyLoggedin.values():
                print("User already logged in.")
            else:
                print("Invalid Credentials.")

        case 2:
            print("INITIATE LOGOUT.")
            # getting individual keys and values from the userCredential
            username = userCredential.keys()
            password = userCredential.values()
            # logout process
            inpusername = input("Enter your User Name: ")
            inppassword = input("Enter your Password: ")
            os.system('cls')
            # Credential check
            if inpusername in username and inppassword in password and inpusername in alreadyLoggedin:
                print("Logout Successful")
                # removing user from alreadyLoggedin list
                alreadyLoggedin.__delitem__(inpusername)
                numberOfUserLoggedinn -= 1
            elif inpusername not in alreadyLoggedin:
                print("User not logged in.")
            else:
                print("Invalid Credentials.")

        case 3:
            os.system('cls')
            print("Currently logged in users = ", alreadyLoggedin.keys())
            print("There are currently", numberOfUserLoggedinn, " number of user logged in.")

        case 4:
            exit()

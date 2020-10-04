users = {}
status = ""

def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit\n")
    if status == "y":
        OldUser()
    elif status == "n":
        NewUser()





def NewUser():
    CreateLogin = input("Create a Username:")

    if CreateLogin in users:
        print("\nUsername already in use, try another one.\n")
    else:
        createpassw = input("Enter a secure password. Ex.:1234:")
        users[CreateLogin] = createpassw
        print("\nAccount Created!")

#-------------------------
def OldUser():
    login = input("Enter login name:")
    passw = input("Enter your secure password:")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("Oopps guess you are not with, create an account now!\n")
        NewUser()


#--------------------------
while status != "q":
    displayMenu()



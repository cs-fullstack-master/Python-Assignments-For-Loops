import os
import getpass

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("\n")

# Extra-ish Credit Password Checker Ask the user to enter a password. Ask them to confirm the password. If it's not
# equal, keep asking until it's correct or they enter q to quit.


noPassword = True
while noPassword:
    pwd = getpass.getpass("Enter your new password: ")
    if pwd.upper() == 'Q':
        break
    else:
        newpwd = getpass.getpass("Enter your new password again: ")
        if newpwd.upper() == 'Q':
            break
        else:
            if pwd.upper() != newpwd.upper():
                print("\nPasswords do NOT Match! Try Again.\n")
            else:
                print("Password Changed Successfully")
                break

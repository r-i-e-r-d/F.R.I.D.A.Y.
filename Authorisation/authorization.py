import getch
import sys
import re
import os


def userName():
    username = input("Enter The Username : ")
    return username


def password():
    print("Enter the Password : ", end="")
    passString = ""
    while True:
        c = getch.getch()
        if c == "\n":
            return passString
        elif ord(c) == 127:
            if len(passString) > 0:
                sys.stdout.write("\x08 \x08")
                sys.stdout.flush()
                passString = passString[0:-1]
            continue
        else:
            sys.stdout.write("*")
            sys.stdout.flush()
            passString += c
    return passString


def passwordCheck(password):
    flag = 0
    while True:
        if len(password) < 8:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("\n\n\t[✔] Password Accepted")
            return flag
    if flag == -1:
        print("\n\n\t[✗] Invalid Password")
        return flag


if __name__ == "__main__":
    os.system("clear")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡  WANT TO BE NEW WORLD  ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ : (Y/n)")
    choice = getch.getch()
    if choice == "y" or choice == "Y":
        username = userName()
        while len(username) == 0:
            username = userName()
        password_Check_flag = -1
        while password_Check_flag != 0:
            passString = password()
            password_Check_flag = passwordCheck(passString)
        directory = "cred"
        parent_dir = "/home/" + username + "/"
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path)
            print("Directory '%s' created successfully" % directory)

        except OSError as error:
            print("Directory '%s' can not be created" % directory)

    else:
        print("\n\n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡  YES YOU DON'T DESERVE THIS WORLD  ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")

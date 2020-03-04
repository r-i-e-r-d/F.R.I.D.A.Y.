import getch
import sys


def userName():
    username = input("Enter The Username : ")
    return username


def password():
    print("Enter the Password : ")
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


if __name__ == "__main__":
    print("************  WANT TO BE NEW WORLD  ************ : (Y/n)")
    choice = getch.getch()
    if choice == "y" or choice == "Y":
        username = userName()
        while len(username) == 0:
            username = userName()
        password = password()
    else:
        print("\n\n************  YES YOU DON'T DESERVE THIS WORLD  ************")

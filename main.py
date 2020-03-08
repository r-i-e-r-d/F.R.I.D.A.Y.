import sys

sys.path.append("/home/devi/F.R.I.D.A.Y./Properties/")
sys.path.append("/home/devi/F.R.I.D.A.Y./Authorisation")
import trav_directory
import authorization

username = "devi"
project = "F.R.I.D.A.Y."

# Comments
#   - make traversal for root directories
#   - make root and superuser account and name other than root
#   - also show username and password
#   - make another file and remove the stuff from this file
#   - this should be home file for superuser account


def just_traverse_directory():
    path = input("Enter the directory name: ")
    traversing_func("/home/" + username + "/" + path)


def list_directories_devi():
    traversing_func("/home/" + username)


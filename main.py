from trav_directory import *

username = 'devil'


# Comments
#   - make traversal for root directories
#   - make root and superuser account and name other than root
#   - also show username and password
#   - make another file and remove the stuff from this file
#   - this should be home file for superuser account

def just_traverse_directory():
    path = input('Enter the directory name: ')
    traversing_func('/home/'+username+'/'+path)


def list_directories_devi():
    traversing_func('/home/'+username)

from trav_directory import *

username = 'devi'


def just_traverse_directory():
    path = input('Enter the directory name: ')
    traversing_func('/home/'+username+'/'+path)


def list_directories_devi():
    traversing_func('/home/'+username)

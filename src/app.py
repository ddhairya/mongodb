from database import Database
from menu import Menu

__author__ = 'dhairya'


Database.initialize()

menu = Menu()
menu.run_menu()

from database import Database
import re
from prettytable import PrettyTable

class User(Database):

    def __init__(self):
        self.SESSION = False
        self.CONTACT = ''

    def login(self):
        email = input('Enter your email : ')
        password  =input('Enter your contact : ')
        emailRegex = '^[A-Za-z0-9.+=]+@[a-z]+\.com'

        if bool(re.search(emailRegex, email)):
            success = Database.user_login(email, password)
            if success:
                if success>0:
                    self.SESSION=True
                    self.CONTACT = password
                    print('Welcome to Canon Gym')
            else:
                print('Please register from admin to continue')
        else:
            print('Invalid email!')

    def logout(self):
        self.SESSION=False

    def view_my_regimen(self):
        if self.SESSION:
            data = Database.view_my_regimen(self.CONTACT)
            table = PrettyTable()
            table.field_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'BMI Start', 'BMI End']
            if data:
                table.add_row(data)
                print(table)       
        else:
            print('You must login first to view your regimen!')

    def view_my_profile(self):
        if self.SESSION:
            data = Database.view_my_profile(self.CONTACT)
            table = PrettyTable()
            table.field_names =  ['Name', 'Email', 'Gender', 'Contact', 'Height', 'Wight', 'Age', 'BMI', 'Membership']
            if data:
                table.add_row(data)
                print(table)       
        else:
            print('You must login first to view your profile!')

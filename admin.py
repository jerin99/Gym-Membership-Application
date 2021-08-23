from prettytable import PrettyTable
from database import Database

import re

class Admin(Database):

    admin = [{'Username':'admin', 'Password':'Password'}]
    #Admins can do their operations only if this session is true
    SESSION = False

    def delete_regimen(self):
        id = int(input('Enter the id of the regimen : '))
        regimen = Database.delete_regimen(id)
        if regimen:
            self.view_regimen()

    def create_regimen(self):
        regimen_list = []
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        print('Please note that start and end BMI\'s are unique')
        start_bmi = float(input('Enter start range of bmi : '))
        end_bmi = float(input('Enter end range of bmi : '))
        for i in range(len(weekdays)):
            day = input('Enter for {} : '.format(weekdays[i]))
            regimen_list.append(day)
        regimen = Database.create_regimen(regimen_list, start_bmi, end_bmi)
        if regimen:
            self.view_regimen()

    def view_regimen(self):
        regimen_list = Database.view_regimen()
        table = PrettyTable()
        table.field_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'BMI Start', 'BMI End']
        for i in range(len(regimen_list)):
            table.add_row(regimen_list[i])
        print(table)


    def delete_user(self):
        phoneRegex = '[0-9]{10}'
        contact = input('Enter contact number to update : ')
        if bool(re.search(phoneRegex, contact)):
            print(Database.delete_user(contact))
        else:
            print('Please enter contact in correct format!')


    def update_user(self):
        phoneRegex = '[0-9]{10}'
        contact = input('Enter contact number to update : ')
        if bool(re.search(phoneRegex, contact)):
            print('1. Name')
            print('2. Email')
            print('3. Gender')
            print('4. Height and Weight')
            print('5. Age')
            print('6. Membership')
            fields = ['name', 'email', 'gender', 'height', 'weight', 'age', 'membership']
            field = int(input('Choose the correct field : '))
            if field==1:
                user_list = Database.update_user(contact, fields[0])
            elif field==2:
                user_list = Database.update_user(contact, fields[1])
            elif field==3:
                user_list = Database.update_user(contact, fields[2])
            elif field==4:
                user_list = Database.update_user(contact, fields[3], fields[4])
            elif field==5:
                user_list = Database.update_user(contact, fields[5])
            elif field==6:
                user_list = Database.update_user(contact, fields[6])
            else:
                print('Invalid option!')

            if user_list==0:
                self.view_user(contact)
        
        else:
            print('Please enter contact in correct format!')

    def view_user(self, contact=0):
        phoneRegex = '[0-9]{10}'
        if contact==0:
            contact = input('Enter contact number : ')
            if bool(re.search(phoneRegex, contact)):
                user_list = Database.view_user(contact)
                table = PrettyTable()
                table.field_names = ['Name', 'Email', 'Gender', 'Contact', 'Height', 'Wight', 'Age', 'BMI', 'Membership']
                if user_list:
                    table.add_row(user_list)
                    print(table)
            else:
                print('Please enter contact in correct format!')
        else:
            if bool(re.search(phoneRegex, contact)):
                user_list = Database.view_user(contact)
                table = PrettyTable()
                table.field_names = ['Name', 'Email', 'Gender', 'Contact', 'Height', 'Wight', 'Age', 'BMI', 'Membership']
                if user_list:
                    table.add_row(user_list)
                    print(table)                
            else:
                print('Please enter contact in correct format!')

    def create_user(self):
        emailRegex = '^[A-Za-z0-9.+=]+@[a-z]+\.com'
        phoneregex = '[0-9]{10}'
        name = input('Enter name : ')
        email = input('Enter email : ')
        if bool(re.search(emailRegex, email)):
            contact = input('Enter contact number : ')
            if bool(re.search(phoneregex, contact)):
                # try:
                gender = input('Enter gender : ')
                age = int(input('Enter age : '))
                height = float(input('Enter height (in CM) : '))
                weight = float(input('Enter weight (in KG) : '))
                duration = int(input('Enter duration (1,3,6 or 12 months) : '))
                dur = [1,3,6,12]
                if duration in dur:
                    print(Database.insert_user(name, email, gender, contact, height, weight, age, duration))
                else:
                    print('Please enter duration only in selected format!')
                # except:
                #     print('Invalid details entered')
            else:
                print('Please check the contact number!')
        else:
            print('You have entered mail in wrong format')
        

    #This class method is used for admin to log into the system
    @classmethod
    def admin_login(cls):
        username = input('Enter your username : ')
        password = input('Enter your password : ')
        for i in range(len(cls.admin)):
            if cls.admin[i]['Username']==username:
                if cls.admin[i]['Password']==password:
                    cls.SESSION = True
                    print('Welcome to Canon Gym Admin Panel')
                else:
                    print('You have entered wrong password!')
            else:
                print('You have entered wrong username!')

    # This class method is used for admin to log out of the system
    @classmethod
    def admin_logout(cls):
        if cls.SESSION==True:
            cls.SESSION = False
            print('You have logged out successfully from Canon\'s Admin Panel')
        else:
            print('You are not logged in!')

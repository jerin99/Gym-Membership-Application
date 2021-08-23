import sqlite3 as sq
from typing import NewType
import re

class Database:

    USER_ID = 100

    #All the user details are stored here
    #Structure[id, Name, Email, Weight, Height]
    USERS = []

    def insert_user(name, email, gender, contact, height, weight, age, membership):
        bmi = (weight/(height*height)*10000)
        bmi = round(bmi,1)
        
        conn = sq.connect('gym_database.db')
        try:
            sql = "INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)"
            values = (None, name, email, gender, contact, height, weight, age, bmi, membership)
            conn.execute(sql, values)
            conn.commit()
            conn.close()
            return 'User has been successfully added'
        except:
            conn.close()
            return 'This contact already exists!'
        
    def view_user(contact):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS")
        for row in query:
            cursor.execute("select name from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)==0:
                print('User doesnt exist!')
            else:
                user_list = []
                for i in range(1,10):
                    user_list.append(row[i])
                return user_list
        conn.close()



    def update_user(contact, field1, field2=0):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS")
        for row in query:
            cursor.execute("select name from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)==0:
                print('User doesnt exist!')
            else:
                if field2==0:
                    if field1=='name':
                        new_value = input('Enter new value : ')
                        sql = "update USERS set name=?"
                        conn.execute(sql, (new_value,))
                        conn.commit()
                        print('Name has been updated successfully')
                        return 0
                    elif field1=='email':
                        emailRegex = '^[A-Za-z0-9.+=]+@[a-z]+\.com'
                        new_value = input('Enter new value : ')

                        if bool(re.search(emailRegex, new_value)):
                            sql = "update USERS set email=?"
                            conn.execute(sql, (new_value,))
                            conn.commit()
                            print('Email has been updated successfully')
                            return 0
                        else:
                            print('Please enter mail in correct format!')
                    elif field1=='gender':
                        new_value = input('Enter new value : ')
                        sql = "update USERS set gender=?"
                        conn.execute(sql, (new_value,))
                        conn.commit()
                        print('Gender has been updated successfully')
                        return 0
                    elif field1=='age':
                        new_value = input('Enter new value : ')
                        sql = "update USERS set age=?"
                        conn.execute(sql, (new_value,))
                        conn.commit()
                        print('Age has been updated successfully')
                        return 0
                    elif field1=='membership':
                        new_value = input('Enter new value : ')
                        dur = [1,3,6,12]
                        if new_value in dur:
                            sql = "update USERS set membership=?"
                            conn.execute(sql, (new_value,))
                            conn.commit()
                            print('Membership has been updated successfully')
                            return 0
                        else:
                            print('You can only shoose from 1, 3, 6 or 12 month plan!')
                else:
                    # try:
                    bmi = 0
                    height = float(input('Enter height : '))
                    weight = float(input('Enter weight : '))
                    bmi = (weight/(height*height)*10000)
                    bmi = round(bmi,1)
                    sql = "update USERS set height=?, weight=?, bmi=?"
                    conn.execute(sql, (height, weight, bmi))
                    conn.commit()
                    print('Height, Weight and BMI updated successfully')
                    return 0
                    # except:
                    #     print('Please enter values in correct format!')

        conn.close()

import sqlite3 as sq
import re

class Database:

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
        query = conn.execute("SELECT * from USERS where contact=?", (contact,))
        for row in query:
            cursor.execute("select contact from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)!=0:
                user_list = []
                for i in range(1,10):
                    user_list.append(row[i])
                return user_list
                
        else:
            print('User doesnt exist!')
        conn.close()



    def update_user(contact, field1, field2=0):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS where contact=?", (contact,))
        for row in query:
            cursor.execute("select name from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)!=0:
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
                        new_value = int(input('Enter new value : '))
                        sql = "update USERS set age=?"
                        conn.execute(sql, (new_value,))
                        conn.commit()
                        print('Age has been updated successfully')
                        return 0
                    elif field1=='membership':
                        new_value = int(input('Enter new value : '))
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
                    try:
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
                    except:
                        print('Please enter values in correct format!')
                
        else:
            print('User doesnt exist!')
        conn.close()


    def delete_user(contact):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS where contact=?", (contact,))
        for row in query:
            cursor.execute("select name from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)!=0:
                sql = "delete from USERS where contact=?"
                conn.execute(sql, (contact,))
                conn.commit()
                return 'User successfully deleted'
                
        else:
            print('User doesnt exist!')
        conn.close()
    
    def view_all_users():
        conn = sq.connect('gym_database.db')
        sql = 'select * from USERS'
        result = conn.execute(sql)
        user_list = []
        for i in result:
            temp_list = []
            for j in range(1, 10):
                temp_list.append(i[j])
            user_list.append(temp_list)
        conn.close()
        return user_list
        
    

    def create_regimen(regimen_list, start_bmi, end_bmi):
        sun = regimen_list[0]
        mon = regimen_list[1]
        tue = regimen_list[2]
        wed = regimen_list[3]
        thu = regimen_list[4]
        fri = regimen_list[5]
        sat = regimen_list[6]

        conn = sq.connect('gym_database.db')
        try:
            sql = "INSERT INTO REGIMEN VALUES(?,?,?,?,?,?,?,?,?,?)"
            values = (None, sun, mon, tue, wed, thu, fri, sat, start_bmi, end_bmi)
            conn.execute(sql, values)
            conn.commit()
            conn.close()
            print('Regimen has been successfully added')
            return 0
        except:
            sql = "update REGIMEN set sun=?, mon=?, tue=?, wed=?, thu=?, fri=?, sat=? where bmi_start=? and bmi_end=?"
            conn.execute(sql, (sun, mon, tue, wed, thu, fri, sat, start_bmi, end_bmi))
            conn.commit()
            print('Regimen has been updated successfully')
            return 0


    def view_regimen():
        conn = sq.connect('gym_database.db')
        sql = 'select * from REGIMEN'
        result = conn.execute(sql)
        regimen_list = []
        for i in result:
            temp_list = []
            for j in range(1, 10):
                temp_list.append(i[j])
            regimen_list.append(temp_list)
        conn.close()
        return regimen_list


    def delete_regimen(id):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from REGIMEN where id=?", (id,))
        for row in query:
            cursor.execute("select id from REGIMEN where id=?", (id,))
            data = cursor.fetchall()
            if len(data)!=0:
                sql = "delete from REGIMEN where id=?"
                conn.execute(sql, (id,))
                conn.commit()
                print('Regimen has been successfully deleted')
                return 0
                
        else:
            print('Regimen doesnt exist with this ID!')
        conn.close()

# ****************************************************************USERS***************************************************8

    def user_login(username, password):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS where email=? and contact=?", (username,password))
        for row in query:
            cursor.execute("select name from USERS where email=? and contact=?", (username,password))
            data = cursor.fetchall()
            if len(data)!=0:
                membership = row[9]
                return membership
                
        else:
            print('User doesnt exist!')
                
        conn.close()
        
    def view_my_regimen(contact):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS where contact=?", (contact,))
        for row in query:
            cursor.execute("select contact from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)!=0:
                bmi = row[8]
                regimen_query = conn.execute("SELECT * from REGIMEN where bmi_end<?", (bmi,))
                for regimen_row in regimen_query:
                    cursor.execute("select * from REGIMEN where bmi_end<?", (bmi,))
                    data = cursor.fetchall()
                    regimen_list = []
                    for i in range(1,10):
                        regimen_list.append(regimen_row[i])
                    return regimen_list
                    break
        conn.close()

    def view_my_profile(contact):
        conn = sq.connect('gym_database.db')
        cursor = conn.cursor()
        query = conn.execute("SELECT * from USERS where contact=?", (contact,))
        for row in query:
            cursor.execute("select name from USERS where contact=?", (contact,))
            data = cursor.fetchall()
            if len(data)!=0:
                user_list = []
                for i in range(1,10):
                    user_list.append(row[i])
                return user_list
        conn.close()
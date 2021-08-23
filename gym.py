from admin import Admin
from user import User

class Gym(Admin, User):
    user = User()
    admin = Admin()
    j=1
    try:
        while j!=0:
            print('\n***********************************')
            print('|| Select any one of the options ||')
            print('***********************************')
            print('** | 1.| User                    **')
            print('** | 2.| Admin                   **') 
            print('** | 3.| Exit                    **') 
            print('***********************************')
            req = int(input('Enter input : '))
            if req==1:
                i = 1
                try:
                    while i!=0:
                        print('\n***********************************')
                        print('|| Select any one of the options ||')
                        print('***********************************')
                        print('** | 1.| Login to Canon gym      **')
                        print('** | 2.| View Your Regimens      **') 
                        print('** | 3.| View Your Profile       **')
                        print('** | 4.| Logout                  **')
                        print('***********************************')
                        req = int(input('Enter input : '))
                    
                        if req==1:
                            user.login()
                        elif req==2:
                            user.view_my_regimen()
                        elif req==3:
                            user.view_my_profile()
                        elif req==4:
                            user.logout()
                            i=0
                        else:
                            print('Invalid input')
                except:
                    print('No option selected! Program exiting users...........', end=" ")
            elif req==2:
                i = 1
                try:
                    while i!=0:
                        print('\n**************************************')
                        print('||   Select any one of the options   ||')
                        print('***************************************')
                        print('** | 1.| Admin Login                 **')
                        print('** | 2.| Create User               **') 
                        print('** | 3.| View User                  **')
                        print('** | 4.| Update User               **')
                        print('** | 5.| Delete User                **')
                        print('** | 6.| Add Books                   **')
                        print('** | 7.| View Regimen         **')
                        print('** | 8.| Create Regimen     **')
                        print('** | 9.| Delete Regimen              **')
                        print('** | 10.| Logout                     **')
                        print('***************************************')
                        req = int(input('Enter input : '))
                        
                        if req==1:
                            admin.admin_login()
                        elif req==2:
                            admin.create_user()
                        elif req==3:
                            admin.view_user()
                        elif req==4:
                            admin.update_user()
                        elif req==5:
                            admin.delete_user()
                        elif req==6:
                            admin.add_books()
                        elif req==7:
                            admin.view_regimen()
                        elif req==8:
                            admin.create_regimen()
                        elif req==9:
                            admin.delete_regimen()
                        elif req==10:
                            admin.admin_logout()
                            i=0
                            print('Thank you')
                        else:
                            print('Invalid input')
                except:
                    print('No option selected! Program exiting admin...........', end=" ")
                    print("\U0001F61F")
            elif req==3:
                print('Thank you for Canon Club Gym uLibrary')
                break
            else:
                print('Invalid input')
    except:
        print('No option selected! Program stopping...........', end=" ")

a = Gym()

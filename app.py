import os, sys
from users import User

def main_menu(error_msg):
    """
    lists all functionality of the site
    """
    menu_choices = [1,2,3,99]
    star_divider = '*' * 35
    line_divider = '-' * 35

    #check for error messages
    if not error_msg:
        #introduce the app
        print(star_divider)
        print ('* Welcome to The comments App!    *')
        print ('%s \n\n' % star_divider)
    else:
        #give user the error message
        print (star_divider)
        print(error_msg)
        print (star_divider)
        #clear error message
        error_msg = None

    #show other options
    print('Select an action from the menu below:\n')
    print('1. Register\n')
    print('2. Login\n')
    print('3. Add comments\n')
    print('%s \n' % line_divider)
    print('99. ****Quit appication****\n')
    print('%s \n' % line_divider)
    choice = int(input('choice >>'))

    #validate choice
    
    if choice not in menu_choices:
        error_msg = 'Invalid choice! Please enter a number from the actions list!'
        main_menu(error_msg)

    if choice == 1:
        user.sign_up()
        print(user.users)
       
        main_menu(error_msg=None)

    if choice == 2:
        user = User()
        user.login()
        main_menu(error_msg=None)



    if choice == 3:
        create_comments()
        main_menu(error_msg=None)
      
    if choice == 99:
        print ('\n%s \n' % star_divider)
        print ('Application will exit now!\n\n')
        sys.exit()

if __name__ == '__main__':
    main_menu(error_msg=None)
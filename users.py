# functions
class User:
    users = [
    {
            'id':1,
            'name':'Admin',
            'password':'admin',
            'role':'admin',
            'email':'admin@gmail.com'
        },
        {
            'id':2,
            'name':'Moderator_one',
            'password':'Moderator_one',
            'role':'moderator',
            'email':'Moderator_one@gmail.com'
        },
        {
             'id':3,
            'name':'Moderator_two',
            'password':'Moderator_two',
            'role':'moderator',
            'email':'Moderator_two@gmail.com'
        }
]

    current_id = 3
    def sign_up(self,name,username,email,password):
        
        User.current_id += 1 
        user = {
                'id':User.current_id ,
                'name':name,
                'username':username,
                'email':email,
                'password':password,
                'role':'common'
            }
        User.users.append(user)

        return user

    def login(self, username, password):
		username = input("Enter your username")
		password = input("Enter your password")
		if username in Users.user:
			if password == Users.user['username'][2]:
				print ('Successfully logged in')
			else:
				print ('invalid password')
		else:
			print ('Username doese not exist')
			











            

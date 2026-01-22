class Username:

    def __init__(self, username, email, is_active = False):
        self.username = username
        self.email = email
        self.is_active = is_active
        

user01 = Username('Bobur', 'Bobur@gmail.com', True)
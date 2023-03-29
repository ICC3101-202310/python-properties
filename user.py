class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) > 3:
            self.__username = value
        else:
            self.__username = value * 3

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if self.__password == value['current_pwd']:
            self.__password = value['new_pwd']
class PasswordManager:
    def __init__(self,password):
        self.__password=password
    
    def verify_password(self,inp):
        return self.__password==inp
    # TODO: Implement the verify_password method




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False

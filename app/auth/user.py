class User:
    def __init__(self, email):
        self.email = email

    #needed by flask-login
    def get_id(self):
        return self.email

    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def is_auth(self):
        return True

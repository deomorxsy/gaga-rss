MOCKING_u = {'grayfoxjumpingover@email.com': '123456'}

class MockDBHelper:
    def get_user(self, email):
        if email in MOCKING_u:
            return MOCKING_u[email]
        return None


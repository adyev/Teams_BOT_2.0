from User import User

class Secretary:
    def __init__(self) -> None:
        self.users: list[User] = []
        pass


    
    def create_test_users(self):
        self.users.extend([
            User(name='Адыев1', chat_id='@1'),
            User(name='Адыев2', chat_id='@1')
        ])
        pass

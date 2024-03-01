import datetime
from User import User
from colored_print import log

class Logger:
    def __init__(self) -> None:
        self.log_file = 'logs.txt'
 
        pass

    #Если юзера нет, по дефолту передается 
    def full_log(self, action: str, user: User = User(chat_id='no_email', name='Бот')):
        self.console_log(action, user)
        self.file_log(action, user)
        
    
    def console_log(self, action: str, user: User = User(chat_id='no_email', name='Бот')):
           log.pink(f'# LOG:  date: {datetime.datetime.now()}, action: {action}, user: {user.name}')

    def file_log(self, action: str, user: User = User(chat_id='no_email', name='Бот')):
        with open (self.log_file, 'r', encoding="UTF-8") as f:
             logs = f.readlines()
             #log.success(logs)
        with open (self.log_file, 'w', encoding="UTF-8") as f:
             logs.insert(0, f'date: {datetime.datetime.now()}, action: {action}, user: {user.name}\n')
             f.writelines(logs)
        pass
from Secretary import Secretary
from User import User
import datetime
import DataFuncs

import config as config

def main():
    s = Secretary()
    #s.logger.clear_log_file()
    #DataFuncs.set_users()
    user: User = s.get_user_by_id(chat_id='adyevdv@sovcombank.ru')
    s.start()
    
    #s.create_test_users()    

if __name__ == '__main__':
    
    #DataFuncs.get_senders()
    main()
    #set_users()
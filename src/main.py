from Secretary import Secretary
import pickle
from User import User
import datetime
import DataFuncs

import config as config

def main():
    s = Secretary()
    s.start()
    
    s.create_test_users()
    for user in s.users:
        print(str(user))


    
    pass


if __name__ == '__main__':
    
    #DataFuncs.get_senders()
    main()
    #set_users()
from User import User
import os
import pickle
import datetime
from Logger import Logger

logger = Logger()
def get_users() -> list:
    logger.full_log(action='get_users')
    directory = './Data/Users'
    #print(os.listdir(directory))
    users = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'rb') as f:
            users.append(pickle.load(f))
    return users        
    
    

def update_add_user(user: User):
    logger.full_log('update_add_user')
    filename = f'./Data/Users/{user.chat_id}.pickle'
    with open(filename, 'wb') as f:
        pickle.dump(user, f)
    

def senders_data_clear():
    logger.full_log('senders_data_clear')
    with open('./Data/senders.txt', 'w') as f:
        f.write('')

def add_sender(user: User):
    logger.full_log('add_sender')
    with open('./Data/senders.txt', 'a') as f:
        f.write(f'{user.chat_id}\n')

def get_senders()->set:
    logger.full_log('get_senders')
    with open('./Data/senders.txt', 'r') as f:
        senders = f.read().splitlines()
        return set(senders)
    
def set_users():
    with open ('Data/Users/adyevdv@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='adyevdv@sovcombank.ru', name='Адыев Дмитрий Владимирович', birth_date=datetime.date(1999, 8, 7), groop='SaA'), f)
    with open ('Data/Users/barancheevai@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='barancheevai@sovcombank.ru', name='Баранчеев Андрей Игоревич', birth_date=datetime.date(1981, 1, 10), groop='SaA'), f)
    with open ('Data/Users/erbulovns@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='erbulovns@sovcombank.ru', name='Ербулов Нурлан Сарсенгалиевич', birth_date=datetime.date(1987, 1, 11), time_zone=1, city='Саратов'), f)
    with open ('Data/Users/emelyanovaov@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='emelyanovaov@sovcombank.ru', name='Емельянова Олеся Витальевна', birth_date=datetime.date(2001, 4, 1), groop='SaA'), f)
    with open ('Data/Users/shabanovie1@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='shabanovie1@sovcombank.ru', name='Шабанов Илья Евгеньевич', birth_date=datetime.date(1995, 4, 3)), f)
    with open ('Data/Users/kholodkovans@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='kholodkovans@sovcombank.ru', name='Холодкова Наталья Сергеевна', birth_date=datetime.date(1993, 4, 10)), f)
    with open ('Data/Users/maiorovkv@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='maiorovkv@sovcombank.ru', name='Майоров Кирилл Валерьевич', birth_date=datetime.date(1986, 7, 16), time_zone=1, city='Саратов'), f)
    with open ('Data/Users/lipniksg@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='lipniksg@sovcombank.ru', name='Липник Сергей Геннадьевич', birth_date=datetime.date(1991, 8, 21), time_zone=7, city='Хабаровск', groop='SaA'), f)
    with open ('Data/Users/ismihanovoa@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='ismihanovoa@sovcombank.ru', name='Исмиханов Олег Александрович', birth_date=datetime.date(1980, 9, 11), time_zone=1, city='Саратов'), f)
    with open ('Data/Users/ryzhovaa@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='ryzhovaa@sovcombank.ru', name='Рыжов Артем Андреевич', birth_date=datetime.date(1993, 9, 24), groop='SaA'), f)
    with open ('Data/Users/korotkovata@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='korotkovata@sovcombank.ru', name='Короткова Татьяна Андреевна', birth_date=datetime.date(1987, 10, 16), time_zone=7, city='Хабаровск'), f)
    with open ('Data/Users/steganovaka@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='steganovaka@sovcombank.ru', name='Стеганова Ксения Алексеевна', birth_date=datetime.date(2001, 10, 26), time_zone=1, city='Саратов', groop='SaA'), f)
    with open ('Data/Users/kitovdv@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='kitovdv@sovcombank.ru', name='Китов Дмитрий Викторович', birth_date=datetime.date(1994, 11, 25), time_zone=7, city='Хабаровск'), f)
    with open ('Data/Users/mizinovvv@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='mizinovvv@sovcombank.ru', name='Мизинов Владимир Владимирович', birth_date=datetime.date(1988, 12, 14), time_zone=1, city='Саратов'), f)
    with open ('Data/Users/shilovaev@sovcombank.ru.pickle', 'wb') as f:
        pickle.dump(User(chat_id='shilovaev@sovcombank.ru', name='Шилова Елена Викторовна', birth_date=datetime.date(1986, 5, 22), groop='SaA'), f)
    

    
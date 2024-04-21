from User import User
from Group import Group
import os
import pickle
import datetime
from Logger import Logger
import psycopg2
from psycopg2.extras import DictCursor
import config

logger = Logger()

def SQL_Select(query, args):
    rows = ()
    conn = psycopg2.connect(dbname = config.DB_NAME, user = config.DB_USER, 
                        password = config.DB_PASSWORD, host = config.DB_HOST)
    cursor = conn.cursor(cursor_factory=DictCursor)
    try:
        cursor.execute(query, args)
        rows = cursor.fetchall()
    except Exception as e:
        logger.full_log(action=f'!!!EXEPTION: {e}')
    cursor.close()
    conn.close()
    return rows


def SQL_Update(query, args):
    conn = psycopg2.connect(dbname = config.DB_NAME, user = config.DB_USER, 
                        password = config.DB_PASSWORD, host = config.DB_HOST)
    cursor = conn.cursor(cursor_factory=DictCursor)
    try:
        cursor.execute(query, args)
        conn.commit()
    except Exception as e:
        logger.full_log(action=f'!!!EXEPTION: {e}')
        conn.rollback()
    cursor.close()
    conn.close()

def get_group(name):
    row = SQL_Select('select * from "secretary"."TS_GROUPS" g where g."NAME" = %s', (name,))
    return Group(name=row[0]['NAME'], 
                 b_day_man_id=row[0]['ID_BIRTHDAY_MAN'],
                 boss_id=row[0]['ID_BOSS'],
                 chat_id=row[0]['ID_CHAT'])
    pass

def get_group_users(group_name):
    rows = SQL_Select('select * from "secretary"."TS_USERS" u where u."GROUP" = %s', (group_name,))
    users: list[User] = []
    for row in rows:
        users.append(User(name=row['NAME'],
                          chat_id=row['TEAMS_ID'],
                          birth_date=row['BIRTHDAY'],
                          city=row['CITY'],
                          group=row['GROUP'],
                          silenсed=row['SILENCED'],
                          time_zone=row['UTC_DIFF']))
    return users
    pass

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
    SQL_Update('delete from "secretary"."TS_SENDERS"', ())

def add_sender(user: User):
    SQL_Update('INSERT INTO "secretary"."TS_SENDERS" ("TEAMS_ID") VALUES (%s);', (user.chat_id,))

def get_senders(group_name)->set:
    logger.full_log('get_senders')
    rows = SQL_Select(f'SELECT u."TEAMS_ID" ' 
                      f'FROM secretary."TS_USERS" u '
                      f'where 1=1 '
                      f'and u."GROUP" = %s '
                      f'and u."TEAMS_ID" in (select "TEAMS_ID" from secretary."TS_SENDERS" s)', (group_name,))
    senders = set()
    for row in rows:
        senders.add(row['TEAMS_ID'])
    return senders
    

    
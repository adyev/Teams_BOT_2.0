from User import User
from bot.bot import Bot
from bot.handler import MessageHandler
from bot.handler import BotButtonCommandHandler
from schedule import every
from pathos.multiprocessing import ProcessPool
from threading import Thread
from Button import Button
from Logger import Logger
import time
import os
import json
import schedule
import DataFuncs
import config



class Secretary:
    def __init__(self) -> None:
        self.users: list[User] = DataFuncs.get_users()
        self.senders = DataFuncs.get_senders()
        self.bot = Bot(token=os.environ.get("TEAMS_BOT_TOKEN", "localhost:5432"))
        self.logger = Logger()
        self.buttons = {
            'callback_silenced_on': Button(text='Включить', 
                                           callbackData="callback_silenced_on",
                                           callback_func=self.silensed_switch
                                           )
        }


    def start_schedule(self):
        self.logger.full_log(action='start_schedule')
        #every().hour.at(":00").do(daily_question)
        every().day.at("00:00").do(DataFuncs.senders_data_clear)
        #every().day.at("13:00").do(send_report)
        while (True):
            schedule.run_pending()
            time.sleep(1)
        
    def silensed_switch(self, user: User):
        pass

    def get_user_by_id(self, chat_id) -> User:
        for user in self.users:
            if user.chat_id == chat_id:
                return user
        return -1
        

    def start(self):
        thread = Thread(target=self.start_schedule)
        thread.start()
        self.bot.start_polling()
        self.bot.idle()
        pass

    def create_test_users(self):
        self.users.extend([
            User(name='Адыев1', chat_id='@1'),
            User(name='Адыев2', chat_id='@1')
        ])
        pass

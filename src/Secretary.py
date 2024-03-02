from User import User
from bot.bot import Bot
from bot.bot import Event
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
        self.bot.dispatcher.add_handler(MessageHandler(callback=self.message_reaction))
        self.CHAT_ID = os.environ.get("TEAMS_CHAT_ID", "localhost:5432")
        self.logger = Logger()
        self.buttons = {
            'callback_silenced_on': Button(text='Включить', 
                                           callbackData="callback_silenced_on",
                                           callback_func=self.silenсed_swich
                                           )
        }

    
    
    def message_reaction(self, bot: Bot, event: Event):
        commands = ['/start', '/menu', '/help', '/changeCity', '/setWorkTime', '/gimmeChatId']
        #print (event)
        
        user = self.get_user_by_id(chat_id=event.data['from']['userId'])
        if(event.text == '/gimmeChatId'):
            print(event.from_chat)
        if (event.chat_type == 'private'):
            if (user == None):
                bot.send_text(text='Сначала необходимо пройти регистрацию через команду /start', chat_id=event.from_chat)
            elif(event.text in commands):
                self.logger.full_log(action= f'Команда {event.text}, личный чат', user=user)
                if (event.text == '/menu'):
                    self.send_menu(user=user)
                elif(event.text == '/start'):
                    self.register(event=event)
                elif(event.text == '/changeCity'):
                    self.changeCity(user=user)
                elif(event.text == '/setWorkTime'):
                    self.setWorkTime(user=user)
                elif(event.text == '/help'):
                    bot.send_text(text='Список доступных команд:\n'\
                                  '/menu - вызвать основное меню. '\
                                  'В нем можно включить или отключить отправление сообщений по графику, '\
                                  'или вручную запросить выбор места работы.\n'\
                                  '/changeCity - вызвать меню выбора города. '\
                                  'После выбора ежедневное сообщение будет приходить в 9:00 по местному времени.\n'\
                                  '/setWorkTime - вызвать меню выбора времени начала работы. '\
                                  'Ежедневное сообщение будет приходить в выбранное время.', chat_id=event.from_chat)
    
            else:
                bot.send_text(text='Неизвестная  команда. Все доступные команды можно посмотреть через команду /help', chat_id=event.from_chat)
    

            
        else:
            if (event.text in commands):
                self.logger.full_log(action= f'Команда {event.text}, публичный чат', user=user)
                bot.send_text(text='<b>Взаимодействие с ботом вне приватного чата запрещено!</b>', chat_id=event.from_chat, parse_mode='HTML')


    def setWorkTime(self, user: User):
        pass

    def changeCity(self, user: User):
        pass

    def register(self, event: Event):
        pass

    def send_menu(self, user: User):
        pass

    def start_schedule(self):
        self.logger.full_log(action='start_schedule')
        #every().second.do(self.message_reaction)
        #every().hour.at(":00").do(daily_question)
        every().day.at("20:44").do(DataFuncs.senders_data_clear)
        #every().day.at("13:00").do(send_report)
        while (True):
            schedule.run_pending()
            time.sleep(1)
        
    def silenсed_swich(self, user: User):
        self.logger.full_log(action='silensed_switch')
        user.silenсed = False if user.silenсed == True else True
        DataFuncs.update_add_user(user)

    def get_user_by_id(self, chat_id):
        for user in self.users:
            if user.chat_id == chat_id:
                return user
        return None
        

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

    
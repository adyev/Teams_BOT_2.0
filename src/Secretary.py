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
        self.bot.dispatcher.add_handler(BotButtonCommandHandler(callback=self.button_reaction))
        self.SAA_CHAT_ID = os.environ.get("TEAMS_SAA_CHAT_ID", "localhost:5432")
        self.RPI_CHAT_ID = os.environ.get("TEAMS_RPI_CHAT_ID", "localhost:5432")
        self.logger = Logger()
        self.buttons = {
            'callback_on':  Button(text='✅ Включить', 
                                           callbackData="callback_on",
                                           callback_func=self.silenсed_swich
                                           ), 
            'callback_off': Button(text='🚫 Выключить', 
                                           callbackData="callback_off",
                                           callback_func=self.silenсed_swich
                                           ),
            'callback_workplace': Button(text='💻 Выбрать место работы', 
                                           callbackData="callback_workplace",
                                           callback_func=self.send_place_choice
                                           ),
            'callback_office': Button(text='💼 Офис', 
                                           callbackData="callback_office",
                                           callback_func=self.send_chosen_place
                                           ),
            'callback_home': Button(text='🏡 Из дома', 
                                           callbackData="callback_home",
                                           callback_func=self.send_chosen_place
                                           ),
            'callback_remind_later': Button(text='🔔 Напомнить позже', 
                                           callbackData="callback_remind_later",
                                           callback_func=self.send_place_choice
                                           ),
        }
    def send_chosen_place(self):
        print ('send_chosen_place')
        pass

    def remind_later(self, event: Event):
        pass

    def send_place_choice(self, event: Event = None, user: User = None):
        if (user == None):
            user = self.get_user_by_id(event.from_chat)
        
        self.logger.full_log(action='send_place_choice', user=user)        
        self.logger.full_log(action='send_place_choice')
        buttons = [[
            self.buttons['callback_office'].form_dict(),
            self.buttons['callback_home'].form_dict(),
        ],
        [
            self.buttons['callback_remind_later'].form_dict()  
        ]]
        self.bot.send_text(text='Где сегодня работаешь?', 
                  chat_id=user.chat_id, 
                  inline_keyboard_markup='{}'.format(json.dumps(buttons)))
        pass

    def daily_question(self):
        
        self.send_place_choice(user=self.get_user_by_id('adyevdv@sovcombank.ru'))
        pass


    def button_reaction(self, bot: Bot, event: Event):
        self.logger.full_log(action='button_reaction')
        button = self.buttons[event.data['callbackData']]
        button.callback_func(event)

    def message_reaction(self, bot: Bot, event: Event):
        self.logger.full_log(action='message_reaction')
        commands = ['/start', '/menu', '/help', '/changeCity', '/setWorkTime', '/gimmeChatId', '/getMe']
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
                elif(event.text == '/getMe'):
                    bot.send_text(text=f'{str(user)}', chat_id=event.from_chat)
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
        self.bot.send_text(text='hi', chat_id=user.chat_id)
        buttons = [[self.buttons['callback_workplace'].form_dict()]]
        if (user.silenсed):
            buttons[0].append(self.buttons['callback_on'].form_dict())
        else:
            buttons[0].append(self.buttons['callback_off'].form_dict())
        #print (buttons)
        self.bot.send_text(text='Что хочешь сделать?', 
                  chat_id=user.chat_id, 
                  inline_keyboard_markup='{}'.format(json.dumps(buttons)))
        pass

        
    def silenсed_swich(self, event: Event):
        user = self.get_user_by_id(event.from_chat)
        self.logger.full_log(action='silensed_switch')
        self.logger.full_log(action='Переключил silenced', user=user)
        user.silenсed = False if user.silenсed == True else True
        DataFuncs.update_add_user(user)
        new_buttons = [[
            self.buttons['callback_workplace'].form_dict()
        ]]
        if (user.silenсed):
            self.bot.send_text(text='Рассылка успешно отключена', chat_id=user.chat_id)
            new_buttons[0].append(self.buttons['callback_on'].form_dict())
        else:
            self.bot.send_text(text='Рассылка успешно включена', chat_id=user.chat_id)
            new_buttons[0].append(self.buttons['callback_off'].form_dict())
        self.bot.edit_text(inline_keyboard_markup=new_buttons, msg_id=event.data['message']['msgId'], chat_id=event.from_chat, text='Что хочешь сделать?')
    def get_user_by_id(self, chat_id):
        for user in self.users:
            if user.chat_id == chat_id:
                return user
        return None
        

    def start_schedule(self):
        self.logger.full_log(action='start_schedule')
        #every().hour.at(":00").do(daily_question)
        #every().day.at("21:24").do(self.send_place_choice)
        every().minute.do(self.daily_question)
        #every().day.at("13:00").do(send_report)
        while (True):
            schedule.run_pending()
            time.sleep(1)

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

    
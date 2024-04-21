from User import User
from bot.bot import Bot
from Logger import Logger
import datetime
import DataFuncs


class Group:
    def __init__(self, name, chat_id, boss_id, b_day_man_id) -> None:
        self.name: str = name
        self.chat_id: str = chat_id
        self.boss_id: str = boss_id
        self.b_day_man_id: str = b_day_man_id
        self.users: list[User] = DataFuncs.get_group_users(group_name=self.name)
        self.senders: set = DataFuncs.get_senders(self.name)

    def send_report(self, bot: Bot):
        if (len(self.senders) == len(self.users)):
            bot.send_text(chat_id=self.chat_id, text='#REPOPT\nСегодня все сообщили о месте работы! 🔥🔥🔥')
            return 0
        else:
            text = '#REPORT\nПользователи, не сообщившие о месте работы сегодня:\n'
            for user in self.users:
                if (user.chat_id not in self.senders):
                    text += f'{user.name}\n'
            bot.send_text(chat_id=self.chat_id, text=text)
            return 0
        pass

    def send_birthday_info(self, bot: Bot):
        now = datetime.datetime.now().date()
        print (now - self.get_user('adyevdv@sovcombank.ru'))
        pass

    def get_user(self, id):
        for user in self.users:
            if (id == user.chat_id):
                return user
        return None

    
    
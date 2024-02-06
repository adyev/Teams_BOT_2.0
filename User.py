class User:
    #name - имя пользователя
    #chat_id - id личного чата пользователя
    #silensed - заглушил ли пользователь бота
    #time_zone - временная зона относительно Москвы
    #city - город проживания
    def __init__(self, name: str, chat_id: str, silensed = False, time_zone = 4, city = "Новосибирск") -> None:
        self.name = name
        self.chat_id = chat_id
        self.silensed = silensed
        self. time_zone = time_zone
        self.city = city

    #переопределение для вывода в виде словаря    
    def __str__(self) -> str:
        return str({'name': self.name, 'chat_id': self.chat_id, 'silensed': self.silensed, 'time_zone': self.time_zone, 'city': self.city})

    #переопределение для вывода в виде объекта    
    def __repr__(self) -> str:
        return f'User({self.name}, {self.chat_id}, {self.silensed}, {self.time_zone}, {self.city})'
    
    #переопределение равенства 
    def __eq__(self, other: object) -> bool:
        return self.chat_id == other.chat_id

    #переопределение неравенства     
    def __ne__(self, other: object) -> bool:
        return self.chat_id != other.chat_id
        
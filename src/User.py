from datetime import date
class User:
    #name - имя пользователя
    #chat_id - id личного чата пользователя
    #silensed - заглушил ли пользователь бота
    #time_zone - временная зона относительно Москвы
    #city - город проживания
    def __init__(self, name: str, 
                 chat_id: str, 
                 silenсed = False, 
                 time_zone = 4, 
                 city = "Новосибирск", 
                 birth_date: date = None,
                 group:str = 'RPI') -> None:
        self.name = name
        self.chat_id = chat_id
        self.silenсed = silenсed
        self.time_zone = time_zone
        self.shifted_time_zone = time_zone
        self.city = city
        self.birth_date = birth_date
        self.group = group

    #переопределение для вывода в виде словаря    
    def __str__(self) -> str:
        return str({'name': self.name, 
                    'chat_id': self.chat_id, 
                    'silenсed': self.silenсed, 
                    'time_zone': self.time_zone, 
                    'shifted_time_zone': self.shifted_time_zone, 
                    'city': self.city,
                    'birth_date': str(self.birth_date),
                    'groop': self.group
                    })

    #переопределение для вывода в виде объекта    
    def __repr__(self) -> str:
        return f'User({self.name}, {self.chat_id}, {self.silenсed}, {self.time_zone}, {self.shifted_time_zone}, {self.city}, {str(self.birth_date)}, {self.group})'
    
    #переопределение равенства 
    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        return self.chat_id == other.chat_id

    #переопределение неравенства     
    def __ne__(self, other: object) -> bool:
        return self.chat_id != other.chat_id
    
    
        


class Button:
    def __init__(self, text, callbackData, callback_func) -> None:
        self.text: str = text
        self.callbackData: str = callbackData
        self.callback_func: function = callback_func
        pass
    
    def form_dict(self):
        return {"text":self.text, "callbackData": self.callbackData, "style": "primary"}
    
    def __str__(self) -> str:
        return f'text: {self.text}, callbackData: {self.callbackData}, callbackFunc: {self.callback_func.__name__}'
    
    def __repr__(self) -> str:
        return f'Button({self.text}, {self.callbackData}, {self.callback_func.__name__})'
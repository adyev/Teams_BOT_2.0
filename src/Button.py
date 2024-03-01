

class Button:
    def __init__(self, text, callbackData, callback_func) -> None:
        self.text = text
        self.callbackData = callbackData
        self.callback_func = callback_func
        pass
    
    def form_dict(self):
        return {"text":self.text, "callbackData": self.callbackData, "style": "primary"}
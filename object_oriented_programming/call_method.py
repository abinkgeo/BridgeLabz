class Message:
    def __init__(self, text):
        self.text = text


    def display(self):
        return self.text
    
    def __call__(self):
        return "Python"



msg = Message("Hello, World!")
print(msg.display())
print(msg())   

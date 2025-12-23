class Addition:
    
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        if isinstance(other,Addition):
             return self.value+other.value
        raise Exception("Invalid Type")
    

a=Addition(5)
b=Addition(10)
print(a+b)
        
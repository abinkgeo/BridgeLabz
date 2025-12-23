class Addition:
    
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+other.value
    

a=Addition(5)
b=Addition(10)

print(a+b)
        
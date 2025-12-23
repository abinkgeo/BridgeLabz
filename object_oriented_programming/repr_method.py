class Laptop:
    def __init__(self,brand,model,chipset):
        self.brand=brand
        self.model=model
        self.chipset=chipset


    def __repr__(self):
        return f"Laptop( brand = {self.brand} , model= {self.model} , chipset = {self.chipset})"



l1=Laptop("Apple","Mac","M2")
print(l1)
print(repr(l1))


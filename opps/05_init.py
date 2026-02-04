class Chai_data:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size
    def summary(self):
        return f"{self.size} ml and {self.type} chai"
    
chaiObj = Chai_data("masala","200")
print(chaiObj.summary())
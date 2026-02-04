class Chai:
    chai_type = "masala"
    def firstChai(self):
        return self.chai_type

chaiObj = Chai()
print(Chai.firstChai(chaiObj))
chaiObj.firstChai()
chaiObj.chai_type = "iiopip"
print(chaiObj.firstChai())
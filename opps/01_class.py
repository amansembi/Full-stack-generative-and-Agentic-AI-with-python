class Chai:
    chai_type = "masala"

chaiObj = Chai()
print(Chai.chai_type)
chaiObj.chai_type = "ilaichi"
del chaiObj.chai_type
print(chaiObj.chai_type)
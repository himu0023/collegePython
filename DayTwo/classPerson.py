# class person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

class carOne:
    def __init__(self, name, model):
            self.name = name 
            self.model = model

class carTwo:
    def __init__(self,name, model):
         self.name = name
         self.model = model

p1 = carOne("Buggati", 2003)
p2 = carTwo("Pagani", 2009)

print(p1.name, p1.model)
print(p2.name, p2.model)
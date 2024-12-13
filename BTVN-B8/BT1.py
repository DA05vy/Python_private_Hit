class Manufacturer:
    #khoi tao lop nha san xuat
    #identity: Ma NSX
    #location: vi tri
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    def describe(self):
        #in thong tin NSX
        print(f"Identity: {self.identity} - Location: {self.location} ")
        
class Device(Manufacturer):
    # Khoi tao thiet bi
    # name: Ten thiet bi
    # price: Gia thiet bi
    def __init__ ( self, name, price, identity, location):
        self.name = name
        self.price = price
        super().__init__(identity,location)
    def describe(self):
        #in thong tin thiet bi
        print(f"Name: {self.name} - Price: {self.price} ")
        super().describe()
    
device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()
print()
device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()
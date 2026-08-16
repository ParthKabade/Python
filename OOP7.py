class Demo:
    #class varaible
    Value1=10
    Value2=20

    def __init__(self):
        self.No1=11
        self.No2=21

    #Instance method
    def fun(self):
        print("Inside instance method name as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def gun(cls):
        print("Inside instance method name as gun")
        #print(Demo.No1)
        #print(Demo.No2)
        print(cls.Value1)
        print(cls.Value2)

    @staticmethod
    def sun():
        print("Inside static method name as sun")        
        print(Demo.Value1)
        print(Demo.Value2)

dobj = Demo()
#call with object
dobj.gun()
Demo.sun()
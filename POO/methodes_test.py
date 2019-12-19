class MethodTypes:
    name = "Ragnar"

    def instanceMethod(self):
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")


m = MethodTypes()
m.instanceMethod()
m.classMethod()
m.staticMethod()

class Base:
    @classmethod
    def method(csl):
        print("hello from Base")

class Child(Base):
    @classmethod
    def method(csl):
        print("hello from Child")

Base.method() 
Child.method()
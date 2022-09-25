class MyClass:
    i = 21
    def f(self):
        print(self.i)
        self.i = 30
        print(self.i)
    

x = MyClass()
MyClass.i = 10
print(MyClass.i)
x.f()
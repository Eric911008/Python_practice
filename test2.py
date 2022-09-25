class Complex():
    i = 20
    def __init__(self,real,imag):
        self.r = real
        self.i = imag
    
    def __del__(self):
        print("delete object")
    
x = Complex(3.0, -4.5)   
print(Complex.i)
print(x.r,x.i)
x = None
print(x)        

#outer class and inner class eaxmple
class outer:
    def __init__(self):
        print('outer class constructor')
    def m1(self):
        print('m1 in outer class')
    @classmethod
    def m2(cls):
        print('m2 in outer class')
    @staticmethod
    def m3():
        print('m3 in outer')
    class inner:
        def f1(self):
            print('f1 in inner')
        @staticmethod
        def f2():
            print('f2 in inner')

outer().inner.f2()
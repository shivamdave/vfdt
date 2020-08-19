class test():
    a = 1
    print(123)
    print(a)
    def __init__(self, anf, *abc,**bcd):
        self.anf = anf
        print('in the init')
        print(1234)
        print(self.anf)

a = test('1345')
print(a)
print(a)
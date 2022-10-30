#one.py

def func():
    print('Func in one.py')

def func2():
    pass

def func3():
    pass

print('TOP LEVEL in one.py')

if __name__ == '__main__':
   func()
   if not func2():
    func3()


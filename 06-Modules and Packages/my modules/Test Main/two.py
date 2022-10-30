import one

print('TOP level in two.py')

one.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly')
else:
    print('TWO.PY has been IMPORTED')
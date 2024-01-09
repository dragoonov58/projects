a = input()
b = input()
if type(a) == str and type(b) == str:
    if a == b:
        print('1')
    else:
        if len(a) > len(b):
            print('2')
        if b == 'learn':
            print('3')
else:
    print('0')


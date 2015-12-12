def fetcher(obj, index):
    return obj[index]

def f3():
    raise Exception

def f2():
    try:
        f3()
    except:
        print('Exception from f3')
    print('f2 done')

def f1():
    try:
        f2()
    except:
        print('Exception from f2')
    print('f1 done')

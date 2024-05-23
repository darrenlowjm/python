
def okok():
    try:
        raise IOerror
        print('herer')
    except:
        print('exception caught')
        return 'okok'
    else:
        print('no issue')
    finally:
        print('finally')


print(okok() )


with open('water/txt') as fi:
    print('opening is success')
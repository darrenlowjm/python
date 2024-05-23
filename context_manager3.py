from contextlib import contextmanager

a = []

@contextmanager
def something(name):
    a = [1,2,3]
    print('entering')

    try:
        yield a
    finally:
        print('Leaving')

if 0:
    obj = something('name')
    # this return a contextlib._GeneratorContextManager object
    # print(obj)

    #obj.__enter__()

    #In order to yield the contextlib._GeneratorContextManager object, need to run the .__enter__()

    for i in obj.__enter__():
        print(i)

    print('------------------')

if 0:
    with something('peter') as x:
        print(x)
        raise Exception('hit it')

if 1:
    obj = something('name')
    #obj.__enter__()
    #obj.__exit__(None,None,None)

    for i in obj.__enter__():
        print(i)

    result = obj.__exit__(None,None,None)
    print(result)
from contextlib import contextmanager


class Outer_cm:
    def __init__(self, inner_cm):
        self.inner_cm = inner_cm

    def __enter__(self):
        print('Entering outer_cm..')
        self.inner_cm.__enter__()

    def __exit__(self, ex_type, ex_value, ex_tb):
        print('Exiting outer_cm..')
        self.inner_cm.__exit__(ex_type, ex_value, ex_tb)


@contextmanager
def apiFactory():
    print('Starting apiFactory..')

    resource = [1, 2, 3]

    try:
        print('Entering..context')
        yield resource
    finally:
        print('Exiting..context')


if 0:
    # show how an outer cm can call and control an inner cm
    # notice that the outer needs to explicitly call the inner.__enter__ and __exit__
    # in order to activate the inner cm
    with apiFactory() as api:
        print('Go')
        for i in api:
            print(i)

if 1:
    with Outer_cm(apiFactory()) as api:
        print('Go')


if 0:
    apiFactory().__enter__()

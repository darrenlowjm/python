# TODO:
# drive string formatting
import pytest



@pytest.fixture
def dummy(request):
    print('\nstart dummy')
    dummy_var = 1
    yield
    print(f'\nfinally var  = {dummy_var}')

    

def test_1(dummy)    :
    print('i am in')









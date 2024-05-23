import pytest

def setup_module():
    print('I am in setup')

def teardown_module():
    print('I am in teardown')




@pytest.fixture
def fixtures_func():
    print('before yield')
    yield
    print('after yield')



def test_comething(fixtures_func):
    print('testing done')
    assert False, 'I am asserting for Kyaw Swa!'
    
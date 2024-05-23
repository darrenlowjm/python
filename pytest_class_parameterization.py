import pytest










def setup_module():
    print('\n## in setup_module')

def teardown_module():
    print('\n## in teardown_module')






def setup_the_dg(n):
    print(f'test_setup_the_dg: {n}')



def test_01():
    setup_the_dg('8+2')
    print(f'test_simple_case: ')

def test_02():
    print(f'test_weird_simple_case: ')

##############
    
def test_03():
   setup_the_dg('8+3')

def test_04():
    test_02()
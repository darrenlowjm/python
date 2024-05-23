import pytest

# Custom Libraries
import shcore as sw2
from shcore.fixtures import *  # noqa: F403


def setup_module():
    sw2.log.set_log_file(__file__)
    sw2.log.save_file('show_config', sw2.send.cli_cmd('show config', outputformat=sw2.OutputFormat.console))
    sw2.clear_config()


def teardown_module():
    sw2.clear_config()
    sw2.log.summary()





#############
def extract_csv_data():
    print('** Calling extract_csv_data()')
    # can read form external file (json) and return whatever you want in a list.
    # must return a list of objects
    return [('test_1','this is to test something...','p1','p11','p111'),
            ('test_2','this is to test something...','p2','p22','p22'),
            ('test_3','this is to test something...','p31','p3','p333'),]


def id_fn(fixture_value):
    return fixture_value[0]     # returns a nice id that pytest can use to identify a particular testcase set


# fixture
# pytest will create this fixture and call extract_csv_data() which should return a list of objects.
# Based on the number of objects in the list, the test will be executed the same num of iterations
@pytest.fixture(params=extract_csv_data(), ids=id_fn)
def read_csv_fixture(request):
    return request.param
    
    
############


# using fixture        
def xtest_pytest(read_csv_fixture,  fixture_logging)    :
    test_id, desc, test_param1, test_param2, test_param3 = read_csv_fixture
    sw2.log.title(test_ID=test_id, desc=desc)

    print(f'Inside testcase: {read_csv_fixture}')
    


# using parametrize
@pytest.mark.parametrize("print_testid,desc,min_disks,type,level", extract_csv_data())
def test_pytest_parametrizing(print_testid,desc,min_disks,type,level, fixture_logging)    :
    sw2.log.title(test_ID=print_testid, desc=desc)
    print(f'Inside testcase: {min_disks}, {type}, {level}')

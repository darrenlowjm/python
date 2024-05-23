# *** DO NOT CHANGE THE NAME OF THIS FILE (conftest.py) ***
#
# Configuration file for PyTest.
# This file will be automatically be loaded and available for tests
# in this directory and any subdirectories.
#
# It is a good place to put fixtures.  A 'fixture' can be loaded
# prior to tests to pre-populate data.
#
import logging
import sys
import pytest
import shutil
import os

from shcore.utilities.argparse_helper import addOptions, setGlobalVars

from testlib.mc_factory import MCFactory

try:
    import pathlib
except ImportError:
    # Pathlib is built into Python3 but not Python2 (although it
    # is available as a pip-installable module). If the caller
    # doesn't have pathlib, use the one in PyTest.
    from _pytest import pathlib

# Make sure our directory is in the search path for Python files.
SHOCKWAVE_DIR = pathlib.Path(__file__).parent.as_posix().replace('/', os.sep)

#SHOCKWAVE_DIR = os.path.dirname(__file__)
print(SHOCKWAVE_DIR)

#SHOCKWAVE_DIR = os.path.dirname(__file__).replace('\', "\\") 

if SHOCKWAVE_DIR not in sys.path:
    print('adding..shockwave_dir to sys.path')
    #sys.path.append(SHOCKWAVE_DIR)

print(sys.path)
import shcore


def pytest_addoption(parser):
    """
    Hook used to add command line options to pytest.

    :param parser: The PyTest parser object.
    :type parser: The parser object
    """
    addOptions(parser=parser)
    parser.addoption('--repeat', action='store',
        help='Number of times to repeat each test')


def pytest_configure(config):
    """
    Pytest initialization hook.
    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.

    :param config: The Pytest config object
    :type config: _pytest.config.Config
    """    # Add a NULL handler to the root logger to suppress 'no handlers' warning.
    logging.getLogger().addHandler(logging.NullHandler())
    setGlobalVars(config.option)


def pytest_unconfigure(config):
    """
    Pytest initialization hook.
    This hook is called before test process is exited.

    :param config: The Pytest config object
    :type config: _pytest.config.Config
    """
    if shcore.logDirIsTemp and shcore.logDirPath:
        # This is a temporary directory, and we need to remove it.
        # (If the user wanted to keep the logs, they should have
        # given us a place to put them!)
        dirName = str(shcore.logDirPath)
        shutil.rmtree(dirName, ignore_errors=True)


def pytest_generate_tests(metafunc):
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)

        # We're going to duplicate these tests by parametrizing them,
        # which requires that each test has a fixture to accept the parameter.
        # We can add a new fixture like so:
        metafunc.fixturenames.append('tmp_ct')

        # Now we parametrize. This is what happens when we do e.g.,
        # @pytest.mark.parametrize('tmp_ct', range(count))
        # def test_foo(): pass
        metafunc.parametrize('tmp_ct', range(count))

@pytest.fixture
def mc():
    """
    Fixture to return the default MC object.
    :return: The default MC object.
    :rtype: lib.mc_factory.MCFactory
    """
    return MCFactory(ip=shcore.mcIP)

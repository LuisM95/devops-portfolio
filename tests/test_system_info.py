""" Test for  system_info .py
""" 

import os 
import sys 
import platform

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'linux', 'scripts' ))

from system_info import get_system_info


def test_system_info_runs():
    """ Test that system_info runs without errors"""
    try: 
        get_system_info()
        assert True

    except Exceptios as e:
        assert False, f'System info failed with: {e}'


def test_os_is_linux():
    """Test that we are running on Linux"""
    import platform
    assert platform.system() == 'Linux'


def test_working_directory_exists():
    """ Test that the working directory exists"""
    assert os.path.exists(os.getcwd())

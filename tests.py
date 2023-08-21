import unittest
import pyArubaAPI
from globals import *


class TestAuthentication(unittest.TestCase):
    def testManualAuth(self):
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        Switch.authorize()
        assert Switch.call(pyArubaAPI.get_system_info) is not None

    def testAutomaticAuth(self):
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        assert Switch.call(pyArubaAPI.get_system_info) is not None


if __name__ == '__main__':
    unittest.main()

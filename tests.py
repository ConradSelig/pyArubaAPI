import pyjson5
import unittest
import pyArubaAPI

from globals import *


class TestAuthentication(unittest.TestCase):
    def testManualAuth(self):
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        Switch.authorize()
        assert Switch.get("uiGetSystem") is not None

    def testAutomaticAuth(self):
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        assert Switch.get("uiGetSystem") is not None


class TestEndpoints(unittest.TestCase):

    @staticmethod
    def test_uiGetSystem():
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        assert "system_static" in Switch.get("uiGetSystem").json().keys()

    @staticmethod
    def test_uiGetStatus():
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        assert "system_status" in Switch.get("uiGetStatus").json().keys()

    @staticmethod
    def test_getAllVlanInfo():
        Switch = pyArubaAPI.SwitchAPI(switch_ip, switch_username, switch_password)
        response = pyjson5.loads(Switch.get("getAllVlanInfo=", params={"start": 0, "limit": 4095}).text)
        assert response["total"] > 0
        assert len(response["results"]) == response["total"]


if __name__ == '__main__':
    unittest.main()

"""
Unittests for ADVA plugin

"""

__copyright__ = "# Copyright (c) 2020 by cisco Systems, Inc. All rights reserved."
__author__ = "oianson"


import unittest

from unicon import Connection
from unicon.core.errors import SubCommandFailure


class TestADVAPluginConnect(unittest.TestCase):

    def test_connect(self):
        c = Connection(hostname='ADVA',
                       start=['mock_device_cli --os adva --state connect --mock_data_dir mock_data'],
                       os='adva',
                       credentials=dict(
                           default=dict(
                               username='cisco',
                               password='cisco')
                       )
                       )
        c.connect()
        c.settings.POST_DISCONNECT_WAIT_SEC = 0
        c.disconnect()

    def test_truncate_trailing_prompt(self):
        c = Connection(hostname='ADVA',
                       start=['mock_device_cli --os adva --state exec --mock_data_dir mock_data'],
                       os='adva',
                       credentials=dict(
                           default=dict(
                               username='cisco',
                               password='cisco')
                       )
                       )
        c.connect()
        c.settings.POST_DISCONNECT_WAIT_SEC = 0
        output = c.execute('show time') # prompt: ADVA-->
        assert 'ADVA' not in output

        c.execute('network ne-1')  # prompt: ADVA-NE-1-->
        c.execute('configure syncjack', allow_state_change=True) # prompt: ADVA-NE-1:syncjack-->
        c.execute('configure clock-analysis') # prompt: ADVA-NE-1:syncjack:clock-analysis-->
        output = c.execute('show ptp-clock-probe ptp_clock_probe-1-3') # prompt: ADVA-NE-1:syncjack:clock-analysis-->
        assert 'ADVA' not in output

        c.execute('back')
        c.execute('back', allow_state_change=True)
        c.execute('back')

        c.execute('configure system', allow_state_change=True) # prompt: ADVA:system-->
        output = c.execute('show acl-list') # prompt: ADVA:system-->
        assert 'ADVA' not in output
        c.disconnect()

if __name__ == "__main__":
    unittest.main()

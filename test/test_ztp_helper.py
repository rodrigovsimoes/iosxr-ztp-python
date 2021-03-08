import unittest
from unittest import mock

from lib.ztp_helper import ZtpHelpers

class MockZTPHelper:
    get_netns_path_method = 'lib.ztp_helper.ZtpHelpers.get_netns_path'
    setns_method = 'lib.ztp_helper.ZtpHelpers.setns'

    def mock_get_netns_path(*args, **kwargs):
        vrf_file = '/tmp/vrf'
        with open(vrf_file, 'w') as f:
            f.write('vrf')
        return vrf_file

class TestZtpHelpers(unittest.TestCase):
    @mock.patch(MockZTPHelper.get_netns_path_method, side_effect=MockZTPHelper.mock_get_netns_path)
    @mock.patch(MockZTPHelper.setns_method)
    def test_download_file(self, mock_get_netns_path, mock_setns):
        zh = ZtpHelpers()
        zh.download_file(file_url='https://github.com/ios-xr/iosxr-ztp-python/blob/master/lib/ztp_helper.py',
                         destination_folder='.')
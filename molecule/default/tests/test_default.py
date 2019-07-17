import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_xrt_installed(host):
    """
    Test that XRT is installed.
    """
    assert host.file("/opt/xilinx/xrt/bin/xbutil").exists

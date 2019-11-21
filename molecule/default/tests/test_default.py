"""Test Ansible role"""
import os
from os.path import join
from itertools import product
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def _aws_only(host):
    """
    Skip test if not on AWS environment.
    """
    if host.ansible.get_variables().get('xilinx_xrt_env') != 'aws':
        pytest.skip('Not on AWS environment')


def _xrt_installed_only(host):
    """
    Skip test if not on AWS environment.
    """
    if not host.ansible.get_variables().get('xilinx_xrt_install', True):
        pytest.skip('XRT not installed')


def test_xrt_installed(host):
    """
    Test that XRT is installed.
    """
    _xrt_installed_only(host)
    assert host.file("/opt/xilinx/xrt/bin/xbutil").exists


def test_xrt_aws_installed(host):
    """
    Test that XRT AWS is installed.
    """
    _aws_only(host)
    _xrt_installed_only(host)
    assert host.file("/opt/xilinx/xrt/bin/awssak").exists


def test_aws_fpga_runtime_installed(host):
    """
    Test that AWS FPGA runtime libraries are installed.
    """
    _aws_only(host)

    if not host.ansible.get_variables().get('aws_fpga_install'):
        pytest.skip('AWS FPGA runtime not installed')

    assert any(host.file(join(join(*path), 'libfpga_mgmt.so')).exists
               for path in product(('/usr/local/', '/usr/'), ('lib', 'lib64')))


def test_aws_fpga_sources_installed(host):
    """
    Test that AWS FPGA sources are installed.
    """
    _aws_only(host)

    path = host.ansible.get_variables().get('aws_fpga_src_install')
    if not path:
        pytest.skip('AWS FPGA source not installed')

    assert host.file(path).exists

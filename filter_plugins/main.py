"""Extra Ansible filters"""


def xrt_kernel(xrt_version, kernel_spec, ansible_facts):
    """
    Return kernel compatible with specified XRT.
    If nothing found, default to latest version.

    Args:
        xrt_version (str): XRT version to install.
        kernel_spec (dict): Kernel specification.
        ansible_facts (dict): Ansible facts.

    Returns:
       str: kernel version.
    """
    family = ansible_facts['os_family']

    if family == 'RedHat':
        dist = ansible_facts['distribution_major_version']
    else:
        dist = ansible_facts['distribution_release'].lower()

    try:
        return kernel_spec[family][dist][xrt_version]
    except KeyError:
        return ""


class FilterModule(object):
    """Return filter plugin"""

    @staticmethod
    def filters():
        """Return filter"""
        return {'xrt_kernel': xrt_kernel}

"""Extra Ansible filters"""

# Packages from Xilinx website
_PACKAGES = {
    '2020.1': 'xrt_202010.2.7.766',
    '2019.2': 'xrt_201920.2.5.309',
    '2019.1': 'xrt_201910.2.2.2250',
    '2018.3': 'xrt_201830.2.1.1794',
    '2018.2': 'xrt_201802.2.1.127'
}

# Packages from AWS developer AMI, CentOS7 only
_AWS_PACKAGES = {
    '2020.1': ('1.9.0/Patches/XRT_2020_1/', 'xrt_202010.2.6.0_7.7.1908'),
    '2019.2': ('1.8.0/Patches/XRT_2019_2/', 'xrt_201920.2.3.0_7.7.1908'),
    '2019.1': ('1.7.0/Patches/XRT_2019_1_RC2/', 'xrt_201910.2.2.0_7.6.1810'),
    '2018.3': ('1.6.0/Patches/XRT_2018_3_RC5/', 'xrt_201830.2.1.0_7.6.1810'),
    '2018.2': ('1.5.0/Patches/XRT_2018_2_XDF_RC5/', 'xrt_201802.2.1.0_7.5.1804')
}

# More recent known kernel version compatible with specified XRT version
# - First level: "ansible_os_family"
# - Second level on RedHat: "ansible_distribution_major_version"
# - Second level on Debian: "ansible_distribution_release" (lower cased)
# - Third level: "xilinx_xrt_version"
_MAX_KERNEL = {
    'RedHat': {
        '7': {
            '2020.1': '3.10.0-1160',
            '2019.1': '3.10.0-1062',
            '2018.3': '3.10.0-957',
            '2018.2': '3.10.0-957'}},
    'Debian': {
        'bionic': {
            '2018.3': '4.18.0',
            '2018.2': '4.18.0'}}}


def _pkg_info(version, name, env, ansible_facts):
    """
    Get package information.

    Args:
        version (str): XRT version.
        name (str): Package name: 'xrt' or 'aws'.
        env (str): Running environment 'xrt' or 'aws'
        ansible_facts (dict): Ansible facts.

    Returns:
        tuple of str: name, source URL
    """
    version = str(version)  # May be interpreted as float in template

    family = ansible_facts['os_family']
    is_rhel7 = (family == 'RedHat' and
                ansible_facts['distribution_major_version'] == '7')

    # Get information depending on environment
    if env == 'aws' and is_rhel7:
        path, core = _AWS_PACKAGES[version]
        base_url = 'https://aws-fpga-developer-ami.s3.amazonaws.com/'
        dist = '-x86_64'
    else:
        core = _PACKAGES[version]
        base_url = 'https://www.xilinx.com/bin/public/openDownload?filename='
        path = ''
        dist = '_' + (
            # RHEL7/Centos7 packages use a fixed distribution version as suffix
            '7.4.1708' if is_rhel7 else
            # Ubuntu packages use distribution version (ex: "18.04")
            ansible_facts['distribution_version'])
        if version >= "2019.2":
            # Architecture information
            dist += '-x86_64' if family == 'RedHat' else '-amd64'

    # Define the package file name
    package = ''.join((
        # Package core name with version information
        core,

        # Linux distribution information
        dist,

        # Package name
        '-', name,

        # Package extension
        '.rpm' if family == 'RedHat' else '.deb'
    ))

    # Define Download URL
    url = ''.join((base_url, path, package))

    return package, url


def xrt_pkg_name(version, name, env, ansible_facts):
    """
    Get package name.

    Args:
        version (str): XRT version.
        name (str): Package name: 'xrt' or 'aws'.
        env (str): Running environment 'xrt' or 'aws'
        ansible_facts (dict): Ansible facts.

    Returns:
        str: Package name.
    """
    return _pkg_info(version, name, env, ansible_facts)[0]


def xrt_pkg_src(version, name, env, ansible_facts):
    """
    Get package source URL.

    Args:
        version (str): XRT version.
        name (str): Package name: 'xrt' or 'aws'.
        env (str): Running environment 'xrt' or 'aws'
        ansible_facts (dict): Ansible facts.

    Returns:
        str: Package source url.
    """
    return _pkg_info(version, name, env, ansible_facts)[1]


def xrt_latest(env, ansible_facts):
    """
    Get latest package version available.

    Args:
        env (str): Running environment 'xrt' or 'aws'
        ansible_facts (dict): Ansible facts.

    Returns:
        str: Latest version
    """
    if (env == 'aws' and ansible_facts['os_family'] == 'RedHat' and
            ansible_facts['distribution_major_version'] == '7'):
        packages = _AWS_PACKAGES
    else:
        packages = _PACKAGES

    return sorted(packages)[-1]


def xrt_kernel(version, ansible_facts):
    """
    Return kernel compatible with specified XRT.
    If nothing found, default to latest version.

    Args:
        version (str): XRT version to install.
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
        return _MAX_KERNEL[family][dist][version]
    except KeyError:
        return ""


class FilterModule(object):
    """Return filter plugin"""

    @staticmethod
    def filters():
        """Return filter"""
        return {'xrt_kernel': xrt_kernel,
                'xrt_pkg_name': xrt_pkg_name,
                'xrt_pkg_src': xrt_pkg_src,
                'xrt_latest': xrt_latest}

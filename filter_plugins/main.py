"""Extra Ansible filters"""

# Packages from Xilinx website
# https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/alveo.html
_BASE_URL = "https://www.xilinx.com/bin/public/openDownload?filename="
_PACKAGES = {
    "2021.1": {
        "RedHat": {
            "7": "xrt_202110.2.11.634_7.6.1810-x86_64-xrt.rpm",
            "8": "xrt_202110.2.11.634_8.1.1911-x86_64-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_202110.2.11.634_16.04-amd64-xrt.deb",
            "bionic": "xrt_202110.2.11.634_18.04-amd64-xrt.deb",
            "focal": "xrt_202110.2.11.634_20.04-amd64-xrt.deb",
        },
    },
    "2020.2": {  # 2020.2.1
        "RedHat": {
            "7": "xrt_202020.2.9.317_7.4.1708-x86_64-xrt.rpm",
            "8": "xrt_202020.2.9.317_8.1.1911-x86_64-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_202020.2.9.317_16.04-amd64-xrt.deb",
            "bionic": "xrt_202020.2.9.317_18.04-amd64-xrt.deb",
        },
    },
    "2020.1": {  # 2020.1.1
        "RedHat": {
            "7": "xrt_202010.2.7.766_7.4.1708-x86_64-xrt.rpm",
            "8": "xrt_202010.2.7.766_8.1.1911-x86_64-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_202010.2.7.766_16.04-amd64-xrt.deb",
            "bionic": "xrt_202010.2.7.766_18.04-amd64-xrt.deb",
        },
    },
    "2019.2": {
        "RedHat": {
            "7": "xrt_201920.2.3.1301_7.4.1708-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_201920.2.3.1301_16.04-xrt.deb",
            "bionic": "xrt_201920.2.3.1301_18.04-xrt.deb",
        },
    },
    "2019.1": {
        "RedHat": {
            "7": "xrt_201910.2.2.2250_7.4.1708-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_201910.2.2.2250_16.04-xrt.deb",
            "bionic": "xrt_201910.2.2.2250_18.04-xrt.deb",
        },
    },
    "2018.3": {  # 2018.3.2
        "RedHat": {
            "7": "xrt_201830.2.1.1794_7.4.1708-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_201830.2.1.1794_16.04-xrt.deb",
            "bionic": "xrt_201830.2.1.1794_18.04-xrt.deb",
        },
    },
    "2018.2": {
        "RedHat": {
            "7": "xrt_201802.2.1.127_7.4.1708-xrt.rpm",
        },
        "Debian": {
            "xenial": "xrt_201802.2.1.127_16.04-xrt.deb",
            "bionic": "xrt_201802.2.1.127_18.04-xrt.deb",
        },
    },
}

# Packages from AWS developer AMI, CentOS 7 and Amazon Linux 2 only
# https://github.com/aws/aws-fpga/blob/master/Vitis/docs/XRT_installation_instructions.md
# XRT 2019.1 and less:
# https://github.com/aws/aws-fpga/blob/master/SDAccel/docs/XRT_installation_instructions.md
_AWS_BASE_URL = "https://aws-fpga-developer-ami.s3.amazonaws.com/"
_AWS_PACKAGES = {
    "2021.1": {
        "RedHat": {
            "2": "1.11.0/Patches/XRT_2021_1/xrt_202110.2.11.0_2-x86_64-xrt.rpm",
            "7": "1.11.0/Patches/XRT_2021_1/xrt_202110.2.11.0_7.9.2009-x86_64-xrt.rpm",
        },
    },
    "2020.2": {
        "RedHat": {
            "2": "1.10.0/Patches/XRT_2020_2/xrt_202020.2.8.0_2-x86_64-xrt.rpm",
            "7": "1.10.0/Patches/XRT_2020_2/xrt_202020.2.8.0_7.9.2009-x86_64-xrt.rpm",
        },
    },
    "2020.1": {
        "RedHat": {  # "2" = Amazon Linux 2
            "2": "1.9.0/Patches/XRT_2020_1/xrt_202010.2.6.0_2-x86_64-xrt.rpm",
            "7": "1.9.0/Patches/XRT_2020_1/xrt_202010.2.6.0_7.7.1908-x86_64-xrt.rpm",
        },
    },
    "2019.2": {
        "RedHat": {
            "7": "1.8.0/Patches/XRT_2019_2/xrt_201920.2.3.0_7.7.1908-xrt.rpm",
        },
    },
    "2019.1": {
        "RedHat": {
            "7": "1.7.0/Patches/XRT_2019_1_0_3/xrt_201910.2.2.0_7.7.1908-xrt.rpm",
        },
    },
    "2018.3": {
        "RedHat": {
            "7": "1.6.0/Patches/XRT_2018_3_RC5/xrt_201830.2.1.0_7.6.1810-xrt.rpm",
        },
    },
    "2018.2": {
        "RedHat": {
            "7": "1.5.0/Patches/XRT_2018_2_XDF_RC5/xrt_201802.2.1.0_7.5.1804-xrt.rpm",
        },
    },
}

# More recent known kernel version compatible with specified XRT version
# - First level: "ansible_os_family"
# - Second level on RedHat: "ansible_distribution_major_version"
# - Second level on Debian: "ansible_distribution_release" (lower cased)
# - Third level: "xilinx_xrt_version"
_MAX_KERNEL = {
    "RedHat": {
        "7": {
            "2020.1": "3.10.0-1160",
            "2019.1": "3.10.0-1062",
            "2018.3": "3.10.0-957",
            "2018.2": "3.10.0-957",
        }
    },
    "Debian": {"bionic": {"2018.3": "4.18.0", "2018.2": "4.18.0"}},
}


def _os_release(ansible_facts):
    """

    Args:
        ansible_facts (dict): Ansible facts.

    Returns:
        tuple of str: OS family, OS distribution.
    """
    family = ansible_facts["os_family"]
    if family == "RedHat":
        dist = ansible_facts["distribution_major_version"]
    else:
        dist = ansible_facts["distribution_release"].lower()
    return family, dist


def _pkg_info(version, name, env, ansible_facts):
    """
    Get package information.

    Args:
        version (str): XRT version.
        name (str): Package component name like 'xrt' or 'aws'.
        env (str): Running environment 'xrt' or 'aws'
        ansible_facts (dict): Ansible facts.

    Returns:
        tuple of str: name, source URL
    """
    version = str(version)  # May be interpreted as float in template
    family, dist = _os_release(ansible_facts)

    if env == "aws":
        try:
            path = _AWS_PACKAGES[version][family][dist]
        except KeyError:
            pass
        else:
            path, package = path.rsplit("/", 1)
            package = _xrt_component_package(name, package)
            return package, "{}{}/{}".format(_AWS_BASE_URL, path, package)

    try:
        package = _PACKAGES[version][family][dist]
    except KeyError:
        raise ValueError("This XRT version is not available for this OS")
    package = _xrt_component_package(name, package)
    return package, _BASE_URL + package


def _xrt_component_package(name, package):
    """
    Get component package filename from base XRT package filename.

    Args:
        name (str): Package component name like 'xrt' or 'aws'.
        package (str): Package filename.

    Returns:
        Component package filename.
    """
    return package[::-1].replace("trx-", ("-" + name)[::-1], 1)[::-1]


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
    family, dist = _os_release(ansible_facts)

    if env == "aws":
        from collections import ChainMap

        all_packages = ChainMap(_PACKAGES, _AWS_PACKAGES)
    else:
        all_packages = _PACKAGES

    for version in sorted(all_packages, reverse=True):
        try:
            _ = all_packages[version][family][dist]
            return version
        except KeyError:
            continue
    raise ValueError("No XRT version found for this OS")


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
    family, dist = _os_release(ansible_facts)
    try:
        return _MAX_KERNEL[family][dist][version]
    except KeyError:
        return ""


class FilterModule(object):
    """Return filter plugin"""

    @staticmethod
    def filters():
        """Return filter"""
        return {
            "xrt_kernel": xrt_kernel,
            "xrt_pkg_name": xrt_pkg_name,
            "xrt_pkg_src": xrt_pkg_src,
            "xrt_latest": xrt_latest,
        }

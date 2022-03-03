"""Extra Ansible filters"""

# Packages from Xilinx website
# https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/alveo.html
_BASE_URL = "https://www.xilinx.com/bin/public/openDownload?filename="
_PACKAGES = {
    "2021.2": {
        "RedHat": {
            "7": "xrt_202120.2.12.427_7.8.2003-x86_64-xrt.rpm",
            "8": "xrt_202120.2.12.427_8.1.1911-x86_64-xrt.rpm",
        },
        "Debian": {
            "bionic": "xrt_202120.2.12.427_18.04-amd64-xrt.deb",
            "focal": "xrt_202120.2.12.427_20.04-amd64-xrt.deb",
        },
    },
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
    "2021.2": {
        "RedHat": {
            "7": "1.12.0/Patches/XRT_2021_2/xrt_202120.2.12.0_7.9.2009-x86_64-aws.rpm",
        },
    },
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
            "2021.2": "3.10.0-1160",
            "2021.1": "3.10.0-1127",
            "2020.2": "3.10.0-1127",
            "2020.1": "3.10.0-1160",
            "2019.1": "3.10.0-1062",
            "2018.3": "3.10.0-957",
            "2018.2": "3.10.0-957",
        },
        "8": {
            "2021.2": "4.18.0-305",
            "2021.1": "4.18.0-240",
            "2020.2": "4.18.0-193",
        },
    },
    "Debian": {
        "xenial": {
            "2021.1": "4.4.0-179",
            "2020.2": "4.4.0-186",
        },
        "bionic": {
            "2021.2": "4.15.0-76",
            "2021.1": "4.15.0-101",
            "2020.2": "4.15.0-101",
            "2020.1": "4.18.0",
            "2019.2": "4.18.0",
            "2019.1": "4.18.0",
            "2018.3": "4.18.0",
            "2018.2": "4.18.0",
        },
        "focal": {
            "2021.2": "5.4.0-88",
            "2021.1": "5.4.0-74",
            "2020.2": "5.4.0-52",
        },
    },
}

# Deployment Target Platform packages (Same base URL as _PACKAGES)
_PLATFORM_PACKAGES = {
    "u50": {
        "2021.2": {
            "Debian": "xilinx-u50_2021.2_2021_1021_1001-all.deb.tar.gz",
            "RedHat": "xilinx-u50_2021.2_2021_1021_1001-noarch.rpm.tar.gz",
        },
        "2021.1": {
            "Debian": "xilinx-u50-gen3x16-xdma-all_1-2784799.deb.tar.gz",
            "RedHat": "xilinx-u50-gen3x16-xdma-noarch_1-2784799.rpm.tar.gz",
        },
        "2020.2": {
            "Debian": "xilinx-u50-gen3x16-xdma-201920_3-3_all.deb.tar.gz",
            "RedHat": "xilinx-u50-gen3x16-xdma-201920_3-1.noarch.rpm.tar.gz",
        },
        "2020.1": {
            "Debian": {
                "xenial": "Xilinx_u50-gen3x16-xdma-201920.3-2784799_16.04_deb.tar.gz",
                "bionic": "Xilinx_u50-gen3x16-xdma-201920.3-2784799_18.04_deb.tar.gz",
            },
            "RedHat": "Xilinx_u50-gen3x16-xdma-201920.3-2784799_noarch_rpm.tar.gz",
        },
        "2019.2": {
            "Debian": {
                "xenial": "xilinx-u50-xdma-201920.1-2699728_16.04.deb",
                "bionic": "xilinx-u50-xdma-201920.1-2699728_18.04.deb",
            },
            "RedHat": "xilinx-u50-xdma-201920.1-2699728.x86_64.rpm",
        },
        "2019.1": {
            "Debian": {
                "xenial": "xilinx-u50-xdma-201910.1-0911_16.04.deb",
                "bionic": "xilinx-u50-xdma-201910.1-0911_18.04.deb",
            },
            "RedHat": "xilinx-u50-xdma-201910.1-0911.x86_64.rpm",
        },
    },
    "u55c": {
        "2021.2": {
            "Debian": "xilinx-u55c_2021.2_2021_1021_1001-all.deb.tar.gz",
            "RedHat": "xilinx-u55c_2021.2_2021_1021_1001-noarch.rpm.tar.gz",
        },
    },
    "u200": {
        "2021.2": {
            "Debian": "xilinx-u200_2021.2_2021_1021_1001-all.deb.tar.gz",
            "RedHat": "xilinx-u200_2021.2_2021_1021_1001-noarch.rpm.tar.gz",
        },
        "2021.1": {
            "Debian": "xilinx-u200-gen3x16-xdma-all_1-3209015.deb_2.tar.gz",
            "RedHat": "xilinx-u200-gen3x16-xdma-noarch_1-3209015.rpm_2.tar.gz",
        },
        "2018.3": {  # 2018.3 to 2020.2
            "Debian": {
                "xenial": "xilinx-u200-xdma-201830.2-2580015_16.04.deb",
                "bionic": "xilinx-u200-xdma-201830.2-2580015_18.04.deb",
            },
            "RedHat": "xilinx-u200-xdma-201830.2-2580015.x86_64.rpm",
        },
    },
    "u250": {
        "2021.2": {
            "Debian": "xilinx-u250_2021.2_2021_1021_1001-all.deb.tar.gz",
            "RedHat": "xilinx-u250_2021.2_2021_1021_1001-noarch.rpm.tar.gz",
        },
        "2021.1": {
            "Debian": "xilinx-u250-gen3x16-xdma-all_3.1-3063142.deb_2.tar.gz",
            "RedHat": "xilinx-u250-gen3x16-xdma-noarch_3.1-3063142.rpm_2.tar.gz",
        },
        "2020.2": {
            "Debian": "xilinx-u250-gen3x16-xdma-platform_3.1-1_all.deb.tar.gz",
            "RedHat": "xilinx-u250-gen3x16-xdma-platform-3.1-1.noarch.rpm.tar.gz",
        },
        "2018.3": {  # 2018.3 to 2020.1
            "Debian": {
                "xenial": "xilinx-u250-xdma-201830.2-2580015_16.04.deb",
                "bionic": "xilinx-u250-xdma-201830.2-2580015_18.04.deb",
            },
            "RedHat": "xilinx-u250-xdma-201830.2-2580015.x86_64.rpm",
        },
    },
    "u280": {
        "2021.1": {
            "Debian": {
                "xenial": "xilinx-u280-xdma-201920.3-3246211_16.04.deb",
                "bionic": "xilinx-u280-xdma-201920.3-3246211_18.04.deb",
                "focal": "xilinx-u280-xdma-201920.3-3246211_18.04.deb",
            },
            "RedHat": "xilinx-u280-xdma-201920.3-3246211.x86_64.rpm",
        },
        "2020.1": {  # 2020.1 and 2020.2
            "Debian": {
                "xenial": "xilinx-u280-xdma-201920.3-2789161_16.04.deb",
                "bionic": "xilinx-u280-xdma-201920.3-2789161_18.04.deb",
            },
            "RedHat": "xilinx-u280-xdma-201920.3-2789161.x86_64.rpm",
        },
        "2019.2": {
            "Debian": {
                "xenial": "xilinx-u280-xdma-201920.1-2699728_16.04.deb",
                "bionic": "xilinx-u280-xdma-201920.1-2699728_18.04.deb",
            },
            "RedHat": "xilinx-u280-xdma-201920.1-2699728.x86_64.rpm",
        },
        "2019.1": {
            "Debian": {
                "xenial": "xilinx-u280-xdma-201910.1-2579327_16.04.deb",
                "bionic": "xilinx-u280-xdma-201910.1-2579327_18.04.deb",
            },
            "RedHat": "xilinx-u280-xdma-201910.1-2579327.x86_64.rpm",
        },
    },
}

_PKG_EXTENSION = {
    "Debian": ".deb",
    "RedHat": ".rpm",
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


def xrt_platform_pkg_src(version, platforms, ansible_facts):
    """
    Get the list packages source URL for each platform.

    Args:
        version (str): XRT version.
        platforms (list of str): Platform.
        ansible_facts (dict): Ansible facts.

    Returns:
        list of dict of str: Packages source url and filenames.
    """
    version = str(version)  # May be interpreted as float in template
    family, dist = _os_release(ansible_facts)
    result = set()
    for platform in platforms:
        # Platform
        try:
            packages = _PLATFORM_PACKAGES[platform]
        except KeyError:
            raise ValueError("Unsupported platform: %s" % platform)

        # XRT version
        try:
            packages = packages[version]
        except KeyError:
            # Get most recent previous version
            try:
                packages = packages[tuple(ver for ver in packages if ver < version)[0]]
            except IndexError:
                raise ValueError(
                    "Platform %s not supported on this XRT version" % platform
                )

        # OS
        packages = packages[family]
        if isinstance(packages, str):
            result.add(packages)
            continue
        try:
            result.add(packages[dist])
        except KeyError:
            raise ValueError("Platform %s not supported on this OS" % platform)
    return [dict(name=name, url=_BASE_URL + name) for name in result]


def xrt_platform_pkg_archives(plt_package_src):
    """
    List platform packages archives files

    Args:
        plt_package_src (list of dict of str): Packages sources.

    Returns:
        list of str: Files.
    """
    return [
        pkg["name"]
        for pkg in plt_package_src
        if pkg["name"].lower().endswith(".tar.gz")
    ]


def xrt_platform_pkg_files(plt_package_src, unarchive, ansible_facts, directory):
    """
    List platform packages files to install.

    Args:
        plt_package_src (list of dict of str): Packages sources.
        unarchive (dict): "unarchive" task with "with_items" result.
        ansible_facts (dict): Ansible facts.
        directory (str): Directory path.

    Returns:
        list of str: Files paths.
    """
    from os.path import join

    ext = _PKG_EXTENSION[_os_release(ansible_facts)[0]]
    files = set(
        pkg["name"] for pkg in plt_package_src if pkg["name"].lower().endswith(ext)
    )
    for result in unarchive.get("results", ()):
        try:
            filenames = result["files"]
        except KeyError:
            continue
        for filename in filenames:
            if filename.lower().endswith(ext):
                files.add(filename)
    return [join(directory, file) for file in files]


def video_sdk_release_dir(unarchive, ansible_facts, directory):
    """
    Get release directory for Xilinx Video SDK.

    Args:
        unarchive (dict): "unarchive" task.
        ansible_facts (dict): Ansible facts.
        directory (str): Directory path.

    Returns:
        str: Release directory.
    """
    from os.path import join
    from re import compile

    dist = ansible_facts["distribution"]
    if ansible_facts["os_family"] == "RedHat":
        dist_version = ansible_facts["distribution_major_version"] + r"\.\d+"
        if dist != "Amazon":
            dist = "RHL"
    else:
        dist_version = ansible_facts["distribution_version"]

    match = compile(
        "".join(
            (
                "^release/U30_",
                dist,
                "_",
                dist_version,
                "_.*$",
            )
        )
    ).match

    for path in sorted(unarchive["files"]):
        if match(path):
            return join(directory, path)

    raise ValueError("No Xilinx Video SDK version found for this OS")


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

    versions = set(_PACKAGES)
    if env == "aws":
        versions.update(_AWS_PACKAGES)

    for version in sorted(versions, reverse=True):
        if env == "aws":
            try:
                _ = _AWS_PACKAGES[version][family][dist]
                return version
            except KeyError:
                pass
        try:
            _ = _PACKAGES[version][family][dist]
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
        return _MAX_KERNEL[family][dist][str(version)]
    except KeyError:
        return ""


def xrt_find_package_path(packages, name):
    """
    Get package path from a list of package from "ansible.builtin.find".

    Args:
        packages (list of dict): XRT packages list.
        name (str): Package name: 'xrt' or 'aws'.

    Returns:
        str: Package path.
    """
    filtered = tuple(
        package["path"]
        for package in packages
        if package["path"].rsplit(".", 1)[0].endswith("-" + name)
    )
    try:
        return filtered[0]
    except IndexError:
        raise ValueError(
            'No package found for "%s" in %s'
            % (name, ", ".join(package["path"] for package in packages))
        )


def xrt_find_devtoolset(ansible_facts):
    """
    Get the latest installed Red Hat Developer Toolset from installed package.

    Args:
        ansible_facts (dict): Ansible facts.

    Returns:
        str: Package path.
    """
    import re

    devtoolset_match = re.compile(r"^devtoolset-\d+$").match
    filtered = sorted(
        (package for package in ansible_facts["packages"] if devtoolset_match(package)),
        key=lambda k: int(k.rsplit("-", 1)[1]),
    )
    try:
        return filtered[-1]
    except IndexError:
        raise ValueError('No "devtoolset-*" package installed')


class FilterModule(object):
    """Return filter plugin"""

    @staticmethod
    def filters():
        """Return filter"""
        return {
            "video_sdk_release_dir": video_sdk_release_dir,
            "xrt_kernel": xrt_kernel,
            "xrt_pkg_name": xrt_pkg_name,
            "xrt_pkg_src": xrt_pkg_src,
            "xrt_platform_pkg_src": xrt_platform_pkg_src,
            "xrt_platform_pkg_files": xrt_platform_pkg_files,
            "xrt_platform_pkg_archives": xrt_platform_pkg_archives,
            "xrt_latest": xrt_latest,
            "xrt_find_package_path": xrt_find_package_path,
            "xrt_find_devtoolset": xrt_find_devtoolset,
        }

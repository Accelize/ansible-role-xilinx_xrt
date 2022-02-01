[![Build Status](https://dev.azure.com/Accelize/DRM/_apis/build/status/Ansible%20-%20Xilinx%20XRT?branchName=master)](https://dev.azure.com/Accelize/DRM/_build/latest?definitionId=25&branchName=master)

# Xilinx XRT Ansible Role

This Ansible role install the [Xilinx XRT](https://github.com/Xilinx/XRT) that is required to run Xilinx FPGA devices based applications.

## Requirements

A compatible Xilinx FPGA device is required on the target host.

The role requires to be run as root on the target host.

## Role Variables

* **xilinx_xrt_install**: If `true`, install XRT.
  Default to `true`.
* **xilinx_xrt_version**: Xilinx XRT version to install.
  Default to the latest available.
* **xilinx_xrt_from_src**:  If `true`, install XRT from sources instead of Xilinx provided packages.
  Default to `false`.
* **xilinx_xrt_env**: XRT specific environment.
  Supported values: `aws`, `azure`.
  If not specified, default to the classical Xilinx XRT environment.
* **xilinx_xrt_platforms**: List of FPGA platforms. If specified, install related deployment target platform packages.
  Supported values in the list: `u50`, `u55c`, `u200`, `u250`, `u280`.
* **xilinx_xrt_ensure_compatible_kernel**: If `true`, ensure the Linux kernel installed is compatible.
  Default to `true`.
* **xilinx_xrt_bashrc**: If `true`, add the source of the XRT setup script to the user `~/.bashrc`.
  Default to `false`.
* **xilinx_xrt_check_fpga**: If `true`, check if XRT is properly installed by trying to detect FPGA.
  Default to `false`.
* **xilinx_xrt_container**: Set this to `true` if running the role inside a container to avoid kernel version mismatch issues.
  Default to `false`.
* **xilinx_xrt_rhel7_devtoolset**: Fallback Red Hat Developer Toolset version to use on RHEL/CentOS 7 if not installed by XRT provided dependencies install script.
  No effect if *xilinx_xrt_from_src* is `false`.
  Default to `9`.

### AWS FPGA

AWS environment support extra variables associated to [AWS FPGA](https://github.com/aws/aws-fpga).

The following is only available when **xilinx_xrt_env** is set to `aws`.

* **aws_fpga_install**: If `true`, install AWS FPGA runtime libraries. 
  Default to `true`.
* **aws_fpga_src_install**: If specified, install AWS FPGA sources in the specified directory.
  Default is to not install sources.
* **aws_fpga_version**: AWS FPGA version to install.
  Default to the latest available.
* **aws_fpga_allow_non_root**: If `true`, allow FPGA devices access to all users or users of a specific group. See *aws_fpga_sdk_others*.
  Default to `false`.
* **aws_fpga_sdk_others**: If `true`, allow FPGA devices access to all users else, allow access to users in the group specified by *aws_fpga_sdk_group*.
  Default to `false`.
  No effect if *aws_fpga_allow_non_root* is `false`.
* **aws_fpga_sdk_group**: Name of the group of users that can access to FPGA devices.
  Default to `fpgauser`.
  No effect if *aws_fpga_allow_non_root* is `false` or aws_fpga_sdk_others is `true`.
* **aws_fpga_sdk_override_group**: If true, do not raise error if the group specified by *aws_fpga_sdk_group* already exists.
  Default to `false`.
  No effect if *aws_fpga_allow_non_root* is `false` or aws_fpga_sdk_others is `true`.
* **aws_fpga_driver**: If specified, install the specified alternate driver.
  If not specified use the default XOCL driver.
  This may require *xilinx_xrt_install* set to `False`.
  Supported values: `xdma`.

### Xilinx Video SDK

Extra variable associated with [Xilinx Video SDK](https://github.com/Xilinx/video-sdk) for Alveo U30/AWS VT1.

* **xilinx_video_sdk_install**: If `true`, install Xilinx video SDK. 
  Default to `true`.
* **xilinx_video_sdk_version**: Xilinx video SDK version to install.
  Default to the latest available.

Note: `xilinx_xrt_install` is automatically set to `false` with the Xilinx video SDK because it already contains XRT.

### Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.xilinx_xrt
```

### Dependencies

The role **accelize.linux_kernel** is required if **xilinx_xrt_ensure_compatible_kernel** is set to `true`.

License
-------

Copyright Accelize 2019, Apache 2.0

Installed components licences:

* [Xilinx XRT license](https://github.com/Xilinx/XRT/blob/master/LICENSE)
* [Xilinx Video SDK license](https://github.com/Xilinx/video-sdk/blob/master/LICENSE.txt)
* [AWS FPGA license](https://github.com/aws/aws-fpga/blob/master/LICENSE.txt)

*This Ansible role is not endorsed or affiliated by Xilinx or AWS.*

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).

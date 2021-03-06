[![Build Status](https://travis-ci.org/Accelize/ansible-role-xilinx_xrt.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-xilinx_xrt)

# Xilinx XRT Ansible Role

This Ansible role install the [Xilinx XRT](https://github.com/Xilinx/XRT) that is required to run Xilinx FPGA devices based applications.

## Requirements

A compatible Xilinx FPGA device is required on the target host.

The role requires to be run as root on the target host.

CentOS 7 is recommanded on AWS since AWS only provides packages for it.

## Role Variables

* **xilinx_xrt_install**: If `true` install XRT.
  Default to `true`.
* **xilinx_xrt_version**: Xilinx XRT version to install.
  Default to the latest available.
* **xilinx_xrt_env**: XRT specific environment.
  Supported values: `aws`.
  Default to the classical Xilinx XRT environment.
* **xilinx_xrt_ensure_compatible_kernel**: If `true`, ensure the Linux kernel installed is compatible.
  Default to `true`.
* **xilinx_xrt_bashrc**: If `true`, add the source of the XRT setup script to the user `~/.bashrc`.
  Default to `false`.

### AWS FPGA

The following is only available when **xilinx_xrt_env** is set to `aws`.

AWS environment support extra variables associated to [AWS FPGA](https://github.com/aws/aws-fpga).

* **aws_fpga_install**; If `true` install AWS FPGA runtime libraries. 
  Default to `true`.
* **aws_fpga_src_install**: If specified, install AWS FPGA sources in the specified directory.
  Default is to not install sources.
* **aws_fpga_version**: AWS FPGA version to install.
  Default to the latest available.
* **aws_fpga_allow_non_root**: If `true`, allow FPGA devices access to users in the group specified by *aws_fpga_sdk_group*.
  Default to `false`.
* **aws_fpga_sdk_group**: Name of the group of users that can access to FPGA devices.
  Default to `fpgauser`.
  No effect if *aws_fpga_allow_non_root* is `false`.
* **aws_fpga_sdk_override_group**: If true, do not raise error if the group specified by *aws_fpga_sdk_group* already exists.
  Default to `false`.
  No effect if *aws_fpga_allow_non_root* is `false`.

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
* [AWS FPGA license](https://github.com/aws/aws-fpga/blob/master/LICENSE.txt)

*This Ansible role is not endorsed or affiliated by Xilinx or AWS.*

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).

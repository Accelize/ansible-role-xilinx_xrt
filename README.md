[![Build Status](https://travis-ci.org/Accelize/ansible-role-xilinx-xrt.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-xilinx-xrt)

Xilinx XRT Ansible Role
=======================

This Ansible role install the [Xilinx XRT](https://github.com/Xilinx/XRT) that is required to run Xilinx FPGA devices based applications.

Requirements
------------

A compatible Xilinx FPGA device is required on the target host.

The role requires to be run as root on the target host.

Role Variables
--------------

* **xilinx_xrt_version**: Xilinx XRT version to install. Default to `2018.3`.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.xilinx_xrt
```

Dependencies
------------

None.

License
-------

Apache 2.0

This Ansible role is not endorsed or affiliated by Xilinx.

* [Xilinx XRT license](https://github.com/Xilinx/XRT/blob/master/LICENSE)

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).

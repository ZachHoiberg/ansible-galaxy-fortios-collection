#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_csf
short_description: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and csf category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.9"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
    
requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    
    system_csf:
        description:
            - Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
        default: null
        type: dict
        suboptions:
            accept_auth_by_cert:
                description:
                    - Accept connections with unknown certificates and ask admin for approval.
                type: str
                choices:
                    - disable
                    - enable
            authorization_request_type:
                description:
                    - Authorization request type.
                type: str
                choices:
                    - serial
                    - certificate
            certificate:
                description:
                    - Certificate. Source certificate.local.name.
                type: str
            configuration_sync:
                description:
                    - Configuration sync mode.
                type: str
                choices:
                    - default
                    - local
            fabric_device:
                description:
                    - Fabric device configuration.
                type: list
                suboptions:
                    access_token:
                        description:
                            - Device access token.
                        type: varlen_password
                    device_ip:
                        description:
                            - Device IP.
                        type: str
                    device_type:
                        description:
                            - Device type.
                        type: str
                        choices:
                            - fortimail
                    https_port:
                        description:
                            - HTTPS port for fabric device.
                        type: int
                    login:
                        description:
                            - Device login name.
                        type: str
                    name:
                        description:
                            - Device name.
                        required: true
                        type: str
                    password:
                        description:
                            - Device login password.
                        type: str
            fabric_object_unification:
                description:
                    - Fabric CMDB Object Unification.
                type: str
                choices:
                    - default
                    - local
            fabric_workers:
                description:
                    - Number of worker processes for Security Fabric daemon.
                type: int
            fixed_key:
                description:
                    - Auto-generated fixed key used when this device is the root. (Will automatically be generated if not set.)
                type: str
            group_name:
                description:
                    - Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.
                type: str
            group_password:
                description:
                    - Security Fabric group password. All FortiGates in a Security Fabric must have the same group password.
                type: str
            management_ip:
                description:
                    - Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.
                type: str
            management_port:
                description:
                    - Overriding port for management connection (Overrides admin port).
                type: int
            saml_configuration_sync:
                description:
                    - SAML setting configuration synchronization.
                type: str
                choices:
                    - default
                    - local
            status:
                description:
                    - Enable/disable Security Fabric.
                type: str
                choices:
                    - enable
                    - disable
            trusted_list:
                description:
                    - Pre-authorized and blocked security fabric nodes.
                type: list
                suboptions:
                    action:
                        description:
                            - Security fabric authorization action.
                        type: str
                        choices:
                            - accept
                            - deny
                    authorization_type:
                        description:
                            - Authorization type.
                        type: str
                        choices:
                            - serial
                            - certificate
                    certificate:
                        description:
                            - Certificate.
                        type: str
                    downstream_authorization:
                        description:
                            - Trust authorizations by this node"s administrator.
                        type: str
                        choices:
                            - enable
                            - disable
                    ha_members:
                        description:
                            - HA members.
                        type: str
                    name:
                        description:
                            - Name.
                        type: str
                    serial:
                        description:
                            - Serial.
                        required: true
                        type: str
            upstream_ip:
                description:
                    - IP address of the FortiGate upstream from this FortiGate in the Security Fabric.
                type: str
            upstream_port:
                description:
                    - The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric .
                type: int
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    fortios_system_csf:
      vdom:  "{{ vdom }}"
      system_csf:
        accept_auth_by_cert: "disable"
        authorization_request_type: "serial"
        certificate: "<your_own_value> (source certificate.local.name)"
        configuration_sync: "default"
        fabric_device:
         -
            access_token: "<your_own_value>"
            device_ip: "<your_own_value>"
            device_type: "fortimail"
            https_port: "11"
            login: "<your_own_value>"
            name: "default_name_13"
            password: "<your_own_value>"
        fabric_object_unification: "default"
        fabric_workers: "16"
        fixed_key: "<your_own_value>"
        group_name: "<your_own_value>"
        group_password: "<your_own_value>"
        management_ip: "<your_own_value>"
        management_port: "21"
        saml_configuration_sync: "default"
        status: "enable"
        trusted_list:
         -
            action: "accept"
            authorization_type: "serial"
            certificate: "<your_own_value>"
            downstream_authorization: "enable"
            ha_members: "<your_own_value>"
            name: "default_name_30"
            serial: "<your_own_value>"
        upstream_ip: "<your_own_value>"
        upstream_port: "33"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import schema_to_module_spec
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_schema_versioning
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_system_csf_data(json):
    option_list = ['accept_auth_by_cert', 'authorization_request_type', 'certificate',
                   'configuration_sync', 'fabric_device', 'fabric_object_unification',
                   'fabric_workers', 'fixed_key', 'group_name',
                   'group_password', 'management_ip', 'management_port',
                   'saml_configuration_sync', 'status', 'trusted_list',
                   'upstream_ip', 'upstream_port' ]
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary

def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data

def system_csf(data, fos):
    vdom = data['vdom']
    system_csf_data = data['system_csf']
    filtered_data = underscore_to_hyphen(filter_system_csf_data(system_csf_data))

    
    return fos.set('system',
                    'csf',
                    data=filtered_data,
                    vdom=vdom)
    

def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404




def fortios_system(data, fos):

    if data['system_csf']:
        resp = system_csf(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_csf'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp



versioned_schema = {
    "type": "dict", 
    "children": {
        "status": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "disable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            ], 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "saml_configuration_sync": {
            "type": "string", 
            "options": [
                {
                    "value": "default", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }, 
                {
                    "value": "local", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }
            ], 
            "revisions": {
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": False
            }
        }, 
        "authorization_request_type": {
            "type": "string", 
            "options": [
                {
                    "value": "serial", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }, 
                {
                    "value": "certificate", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }
            ], 
            "revisions": {
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": False
            }
        }, 
        "upstream_port": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "certificate": {
            "type": "string", 
            "revisions": {
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": False
            }
        }, 
        "fabric_workers": {
            "type": "integer", 
            "revisions": {
                "v6.4.4": True
            }
        }, 
        "fixed_key": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": False, 
                "v6.4.0": False, 
                "v6.4.1": False, 
                "v6.2.0": False, 
                "v6.2.3": True, 
                "v6.2.5": False, 
                "v6.2.7": False, 
                "v6.0.11": True
            }
        }, 
        "fabric_object_unification": {
            "type": "string", 
            "options": [
                {
                    "value": "default", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True
                    }
                }, 
                {
                    "value": "local", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True
                    }
                }
            ], 
            "revisions": {
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True
            }
        }, 
        "management_port": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "group_name": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "trusted_list": {
            "type": "list", 
            "children": {
                "authorization_type": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "serial", 
                            "revisions": {
                                "v6.4.4": True, 
                                "v6.4.0": True
                            }
                        }, 
                        {
                            "value": "certificate", 
                            "revisions": {
                                "v6.4.4": True, 
                                "v6.4.0": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": False
                    }
                }, 
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": False
                    }
                }, 
                "certificate": {
                    "type": "string", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": False
                    }
                }, 
                "ha_members": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "downstream_authorization": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "accept", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "deny", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "serial": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "fabric_device": {
            "type": "list", 
            "children": {
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "access_token": {
                    "type": "string", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True
                    }
                }, 
                "device_ip": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "device_type": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "fortimail", 
                            "revisions": {
                                "v6.0.11": True, 
                                "v6.0.0": True, 
                                "v6.0.5": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": False, 
                        "v6.4.0": False, 
                        "v6.4.1": False, 
                        "v6.2.0": False, 
                        "v6.2.3": False, 
                        "v6.2.5": False, 
                        "v6.2.7": False, 
                        "v6.0.11": True
                    }
                }, 
                "login": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": False, 
                        "v6.4.0": False, 
                        "v6.4.1": False, 
                        "v6.2.0": False, 
                        "v6.2.3": False, 
                        "v6.2.5": False, 
                        "v6.2.7": False, 
                        "v6.0.11": True
                    }
                }, 
                "password": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": False, 
                        "v6.4.0": False, 
                        "v6.4.1": False, 
                        "v6.2.0": False, 
                        "v6.2.3": False, 
                        "v6.2.5": False, 
                        "v6.2.7": False, 
                        "v6.0.11": True
                    }
                }, 
                "https_port": {
                    "type": "integer", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "management_ip": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "accept_auth_by_cert": {
            "type": "string", 
            "options": [
                {
                    "value": "disable", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }, 
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.4.4": True, 
                        "v6.4.0": True
                    }
                }
            ], 
            "revisions": {
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": False
            }
        }, 
        "configuration_sync": {
            "type": "string", 
            "options": [
                {
                    "value": "default", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "local", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            ], 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "upstream_ip": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "group_password": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }
    }, 
    "revisions": {
        "v6.0.0": True, 
        "v6.0.5": True, 
        "v6.4.4": True, 
        "v6.4.0": True, 
        "v6.4.1": True, 
        "v6.2.0": True, 
        "v6.2.3": True, 
        "v6.2.5": True, 
        "v6.2.7": True, 
        "v6.0.11": True
    }
}

def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "system_csf": {
            "required": False, "type": "dict", "default": None,
            "options": { 
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["system_csf"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["system_csf"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        if 'enable_log' in module.params:
            connection.set_option('enable_log', module.params['enable_log'])
        else:
            connection.set_option('enable_log', False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "system_csf")
        
        is_error, has_changed, result = fortios_system(module.params, fos)
        
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)

if __name__ == '__main__':
    main()
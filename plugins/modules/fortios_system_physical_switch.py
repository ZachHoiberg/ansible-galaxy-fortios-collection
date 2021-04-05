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
module: fortios_system_physical_switch
short_description: Configure physical switches in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and physical_switch category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.10"
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

    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    system_physical_switch:
        description:
            - Configure physical switches.
        default: null
        type: dict
        suboptions:
            age_enable:
                description:
                    - Enable/disable layer 2 age timer.
                type: str
                choices:
                    - enable
                    - disable
            age_val:
                description:
                    - Layer 2 table age timer Value.
                type: int
            name:
                description:
                    - Name.
                required: true
                type: str
            port:
                description:
                    - Configure member ports.
                type: list
                suboptions:
                    name:
                        description:
                            - Physical port name.
                        required: true
                        type: str
                    speed:
                        description:
                            - Speed.
                        type: str
                        choices:
                            - auto
                            - 10full
                            - 10half
                            - 100full
                            - 100half
                            - 1000full
                            - 1000half
                            - 1000auto
                            - 10000full
                            - 10000auto
                            - 40000full
                            - 100Gfull
                    status:
                        description:
                            - Interface status.
                        type: str
                        choices:
                            - up
                            - down
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
  - name: Configure physical switches.
    fortios_system_physical_switch:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_physical_switch:
        age_enable: "enable"
        age_val: "4"
        name: "default_name_5"
        port:
         -
            name: "default_name_7"
            speed: "auto"
            status: "up"

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


def filter_system_physical_switch_data(json):
    option_list = ['age_enable', 'age_val', 'name',
                   'port']
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


def system_physical_switch(data, fos):
    vdom = data['vdom']

    state = data['state']

    system_physical_switch_data = data['system_physical_switch']
    filtered_data = underscore_to_hyphen(filter_system_physical_switch_data(system_physical_switch_data))

    if state == "present" or state is True:
        return fos.set('system',
                       'physical-switch',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'physical-switch',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_physical_switch']:
        resp = system_physical_switch(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_physical_switch'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "list",
    "children": {
        "age_enable": {
            "type": "string",
            "options": [
                {
                    "value": "enable",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
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
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "name": {
            "type": "string",
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "age_val": {
            "type": "integer",
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "port": {
            "type": "list",
            "children": {
                "status": {
                    "type": "string",
                    "options": [
                        {
                            "value": "up",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "down",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        }
                    ],
                    "revisions": {
                        "v6.0.11": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.0.5": True
                    }
                },
                "speed": {
                    "type": "string",
                    "options": [
                        {
                            "value": "auto",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "10full",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "10half",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "100full",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "100half",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "1000full",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "1000half",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "1000auto",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "10000full",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "10000auto",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "40000full",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        },
                        {
                            "value": "100Gfull",
                            "revisions": {
                                "v6.0.11": True,
                                "v6.0.0": True,
                                "v6.2.3": True,
                                "v6.0.5": True
                            }
                        }
                    ],
                    "revisions": {
                        "v6.0.11": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.0.5": True
                    }
                },
                "name": {
                    "type": "string",
                    "revisions": {
                        "v6.0.11": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.0.5": True
                    }
                }
            },
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": False,
                "v6.4.1": False,
                "v6.2.0": False,
                "v6.2.3": True,
                "v6.2.5": False,
                "v6.2.7": False,
                "v6.0.11": True
            }
        }
    },
    "revisions": {
        "v6.0.0": True,
        "v6.0.5": True,
        "v6.4.4": True,
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
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "system_physical_switch": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["system_physical_switch"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["system_physical_switch"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "system_physical_switch")

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

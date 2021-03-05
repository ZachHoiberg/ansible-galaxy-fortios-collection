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
module: fortios_wireless_controller_bonjour_profile
short_description: Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connnect
   to networks using Bonjour in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify wireless_controller feature and bonjour_profile category.
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
    
    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    wireless_controller_bonjour_profile:
        description:
            - Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connnect to
               networks using Bonjour.
        default: null
        type: dict
        suboptions:
            comment:
                description:
                    - Comment.
                type: str
            name:
                description:
                    - Bonjour profile name.
                required: true
                type: str
            policy_list:
                description:
                    - Bonjour policy list.
                type: list
                suboptions:
                    description:
                        description:
                            - Description.
                        type: str
                    from_vlan:
                        description:
                            - VLAN ID from which the Bonjour service is advertised (0 - 4094).
                        type: str
                    policy_id:
                        description:
                            - Policy ID.
                        type: int
                    services:
                        description:
                            - Bonjour services for the VLAN connecting to the Bonjour network.
                        type: str
                        choices:
                            - all
                            - airplay
                            - afp
                            - bit-torrent
                            - ftp
                            - ichat
                            - itunes
                            - printers
                            - samba
                            - scanners
                            - ssh
                            - chromecast
                    to_vlan:
                        description:
                            - VLAN ID to which the Bonjour service is made available (0 - 4094).
                        type: str
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
  - name: Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connnect to
     networks using Bonjour.
    fortios_wireless_controller_bonjour_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_bonjour_profile:
        comment: "Comment."
        name: "default_name_4"
        policy_list:
         -
            description: "<your_own_value>"
            from_vlan: "<your_own_value>"
            policy_id: "8"
            services: "all"
            to_vlan: "<your_own_value>"

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


def filter_wireless_controller_bonjour_profile_data(json):
    option_list = ['comment', 'name', 'policy_list' ]
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary

def flatten_multilists_attributes(data):
    multilist_attrs = [[u'policy_list', u'services']]

    for attr in multilist_attrs:
        try:
            path = "data['" + "']['".join(elem for elem in attr) + "']"
            current_val = eval(path)
            flattened_val = ' '.join(elem for elem in current_val)
            exec(path + '= flattened_val')
        except:
            pass

    return data
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

def wireless_controller_bonjour_profile(data, fos):
    vdom = data['vdom']
    
    state = data['state']
    
    wireless_controller_bonjour_profile_data = data['wireless_controller_bonjour_profile']
    wireless_controller_bonjour_profile_data = flatten_multilists_attributes(wireless_controller_bonjour_profile_data)
    filtered_data = underscore_to_hyphen(filter_wireless_controller_bonjour_profile_data(wireless_controller_bonjour_profile_data))

    
    if state == "present" or state == True:
        return fos.set('wireless-controller',
                       'bonjour-profile',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('wireless-controller',
                          'bonjour-profile',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')
    

def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404




def fortios_wireless_controller(data, fos):

    if data['wireless_controller_bonjour_profile']:
        resp = wireless_controller_bonjour_profile(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('wireless_controller_bonjour_profile'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp



versioned_schema = {
    "type": "list", 
    "children": {
        "comment": {
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
        "policy_list": {
            "type": "list", 
            "children": {
                "services": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "all", 
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
                            "value": "airplay", 
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
                            "value": "afp", 
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
                            "value": "bit-torrent", 
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
                            "value": "ftp", 
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
                            "value": "ichat", 
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
                            "value": "itunes", 
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
                            "value": "printers", 
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
                            "value": "samba", 
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
                            "value": "scanners", 
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
                            "value": "ssh", 
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
                            "value": "chromecast", 
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
                "to_vlan": {
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
                "description": {
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
                "from_vlan": {
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
                "policy_id": {
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
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                        "choices": ["present", "absent"]},
        "wireless_controller_bonjour_profile": {
            "required": False, "type": "dict", "default": None,
            "options": { 
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["wireless_controller_bonjour_profile"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["wireless_controller_bonjour_profile"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "wireless_controller_bonjour_profile")
        
        is_error, has_changed, result = fortios_wireless_controller(module.params, fos)
        
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
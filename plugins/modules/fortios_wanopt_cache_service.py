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
module: fortios_wanopt_cache_service
short_description: Designate cache-service for wan-optimization and webcache in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify wanopt feature and cache_service category.
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
    
    wanopt_cache_service:
        description:
            - Designate cache-service for wan-optimization and webcache.
        default: null
        type: dict
        suboptions:
            acceptable_connections:
                description:
                    - Set strategy when accepting cache collaboration connection.
                type: str
                choices:
                    - any
                    - peers
            collaboration:
                description:
                    - Enable/disable cache-collaboration between cache-service clusters.
                type: str
                choices:
                    - enable
                    - disable
            device_id:
                description:
                    - Set identifier for this cache device.
                type: str
            dst_peer:
                description:
                    - Modify cache-service destination peer list.
                type: list
                suboptions:
                    auth_type:
                        description:
                            - Set authentication type for this peer.
                        type: int
                    device_id:
                        description:
                            - Device ID of this peer.
                        type: str
                    encode_type:
                        description:
                            - Set encode type for this peer.
                        type: int
                    ip:
                        description:
                            - Set cluster IP address of this peer.
                        type: str
                    priority:
                        description:
                            - Set priority for this peer.
                        type: int
            prefer_scenario:
                description:
                    - Set the preferred cache behavior towards the balance between latency and hit-ratio.
                type: str
                choices:
                    - balance
                    - prefer-speed
                    - prefer-cache
            src_peer:
                description:
                    - Modify cache-service source peer list.
                type: list
                suboptions:
                    auth_type:
                        description:
                            - Set authentication type for this peer.
                        type: int
                    device_id:
                        description:
                            - Device ID of this peer.
                        type: str
                    encode_type:
                        description:
                            - Set encode type for this peer.
                        type: int
                    ip:
                        description:
                            - Set cluster IP address of this peer.
                        type: str
                    priority:
                        description:
                            - Set priority for this peer.
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
  - name: Designate cache-service for wan-optimization and webcache.
    fortios_wanopt_cache_service:
      vdom:  "{{ vdom }}"
      wanopt_cache_service:
        acceptable_connections: "any"
        collaboration: "enable"
        device_id: "<your_own_value>"
        dst_peer:
         -
            auth_type: "7"
            device_id: "<your_own_value>"
            encode_type: "9"
            ip: "<your_own_value>"
            priority: "11"
        prefer_scenario: "balance"
        src_peer:
         -
            auth_type: "14"
            device_id: "<your_own_value>"
            encode_type: "16"
            ip: "<your_own_value>"
            priority: "18"

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


def filter_wanopt_cache_service_data(json):
    option_list = ['acceptable_connections', 'collaboration', 'device_id',
                   'dst_peer', 'prefer_scenario', 'src_peer' ]
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

def wanopt_cache_service(data, fos):
    vdom = data['vdom']
    wanopt_cache_service_data = data['wanopt_cache_service']
    filtered_data = underscore_to_hyphen(filter_wanopt_cache_service_data(wanopt_cache_service_data))

    
    return fos.set('wanopt',
                    'cache-service',
                    data=filtered_data,
                    vdom=vdom)
    

def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404




def fortios_wanopt(data, fos):

    if data['wanopt_cache_service']:
        resp = wanopt_cache_service(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('wanopt_cache_service'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp



versioned_schema = {
    "type": "dict", 
    "children": {
        "acceptable_connections": {
            "type": "string", 
            "options": [
                {
                    "value": "any", 
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
                    "value": "peers", 
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
        "collaboration": {
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
        "src_peer": {
            "type": "list", 
            "children": {
                "priority": {
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
                "auth_type": {
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
                "ip": {
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
                "encode_type": {
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
                "device_id": {
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
        "dst_peer": {
            "type": "list", 
            "children": {
                "priority": {
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
                "auth_type": {
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
                "ip": {
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
                "encode_type": {
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
                "device_id": {
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
        "prefer_scenario": {
            "type": "string", 
            "options": [
                {
                    "value": "balance", 
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
                    "value": "prefer-speed", 
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
                    "value": "prefer-cache", 
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
        "device_id": {
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
        "wanopt_cache_service": {
            "required": False, "type": "dict", "default": None,
            "options": { 
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["wanopt_cache_service"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["wanopt_cache_service"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "wanopt_cache_service")
        
        is_error, has_changed, result = fortios_wanopt(module.params, fos)
        
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
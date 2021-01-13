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
module: fortios_switch_controller_vlan
short_description: Configure VLANs for switch controller in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify switch_controller feature and vlan category.
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
    switch_controller_vlan:
        description:
            - Configure VLANs for switch controller.
        default: null
        type: dict
        suboptions:
            auth:
                description:
                    - Authentication.
                type: str
                choices:
                    - radius
                    - usergroup
            color:
                description:
                    - Color of icon on the GUI.
                type: int
            comments:
                description:
                    - Comment.
                type: str
            name:
                description:
                    - Switch VLAN name.
                required: true
                type: str
            portal_message_override_group:
                description:
                    - Specify captive portal replacement message override group.
                type: str
            portal_message_overrides:
                description:
                    - Individual message overrides.
                type: dict
                suboptions:
                    auth_disclaimer_page:
                        description:
                            - Override auth-disclaimer-page message with message from portal-message-overrides group.
                        type: str
                    auth_login_failed_page:
                        description:
                            - Override auth-login-failed-page message with message from portal-message-overrides group.
                        type: str
                    auth_login_page:
                        description:
                            - Override auth-login-page message with message from portal-message-overrides group.
                        type: str
                    auth_reject_page:
                        description:
                            - Override auth-reject-page message with message from portal-message-overrides group.
                        type: str
            radius_server:
                description:
                    - Authentication radius server. Source user.radius.name.
                type: str
            security:
                description:
                    - Security.
                type: str
                choices:
                    - open
                    - captive_portal
                    - 8021x
            selected_usergroups:
                description:
                    - Selected user group.
                type: list
                suboptions:
                    name:
                        description:
                            - User group name. Source user.group.name.
                        required: true
                        type: str
            usergroup:
                description:
                    - Authentication usergroup. Source user.group.name.
                type: str
            vdom:
                description:
                    - Virtual domain,
                type: str
            vlanid:
                description:
                    - VLAN ID.
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
  - name: Configure VLANs for switch controller.
    fortios_switch_controller_vlan:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_vlan:
        auth: "radius"
        color: "4"
        comments: "<your_own_value>"
        name: "default_name_6"
        portal_message_override_group: "<your_own_value>"
        portal_message_overrides:
            auth_disclaimer_page: "<your_own_value>"
            auth_login_failed_page: "<your_own_value>"
            auth_login_page: "<your_own_value>"
            auth_reject_page: "<your_own_value>"
        radius_server: "<your_own_value> (source user.radius.name)"
        security: "open"
        selected_usergroups:
         -
            name: "default_name_16 (source user.group.name)"
        usergroup: "<your_own_value> (source user.group.name)"
        vdom: "<your_own_value>"
        vlanid: "19"

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


def filter_switch_controller_vlan_data(json):
    option_list = ['auth', 'color', 'comments',
                   'name', 'portal_message_override_group', 'portal_message_overrides',
                   'radius_server', 'security', 'selected_usergroups',
                   'usergroup', 'vdom', 'vlanid']
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


def switch_controller_vlan(data, fos):
    vdom = data['vdom']

    state = data['state']

    switch_controller_vlan_data = data['switch_controller_vlan']
    filtered_data = underscore_to_hyphen(filter_switch_controller_vlan_data(switch_controller_vlan_data))

    if state == "present" or state == True:
        return fos.set('switch-controller',
                       'vlan',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('switch-controller',
                          'vlan',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_switch_controller(data, fos):

    if data['switch_controller_vlan']:
        resp = switch_controller_vlan(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('switch_controller_vlan'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "list",
    "children": {
        "name": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "color": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "selected_usergroups": {
            "type": "list",
            "children": {
                "name": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                }
            },
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "comments": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "portal_message_override_group": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "vlanid": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "usergroup": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "security": {
            "type": "string",
            "options": [
                {
                    "value": "open",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                {
                    "value": "captive-portal",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                {
                    "value": "8021x",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "auth": {
            "type": "string",
            "options": [
                {
                    "value": "radius",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                {
                    "value": "usergroup",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "portal_message_overrides": {
            "type": "dict",
            "children": {
                "auth_login_failed_page": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                "auth_disclaimer_page": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                "auth_login_page": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                },
                "auth_reject_page": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True
                    }
                }
            },
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "vdom": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        },
        "radius_server": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True
            }
        }
    },
    "revisions": {
        "v6.2.0": True,
        "v6.0.0": True,
        "v6.2.3": True
    }
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "switch_controller_vlan": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["switch_controller_vlan"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["switch_controller_vlan"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "switch_controller_vlan")

        is_error, has_changed, result = fortios_switch_controller(module.params, fos)

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

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

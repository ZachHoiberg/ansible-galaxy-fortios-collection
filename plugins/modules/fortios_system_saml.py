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
module: fortios_system_saml
short_description: Global settings for SAML authentication in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and saml category.
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
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    system_saml:
        description:
            - Global settings for SAML authentication.
        default: null
        type: dict
        suboptions:
            artifact_resolution_url:
                description:
                    - SP artifact resolution URL.
                type: str
            binding_protocol:
                description:
                    - Binding protocol.
                type: str
                choices:
                    - post
            cert:
                description:
                    - Certificate to sign SAML messages. Source certificate.local.name.
                type: str
            default_login_page:
                description:
                    - Choose default login page.
                type: str
                choices:
                    - normal
                    - sso
            default_profile:
                description:
                    - Default profile for new SSO admin. Source system.accprofile.name.
                type: str
            entity_id:
                description:
                    - SP entity ID.
                type: str
            idp_artifact_resolution_url:
                description:
                    - IDP artifact resolution URL.
                type: str
            idp_cert:
                description:
                    - IDP certificate name. Source certificate.remote.name.
                type: str
            idp_entity_id:
                description:
                    - IDP entity ID.
                type: str
            idp_single_logout_url:
                description:
                    - IDP single logout URL.
                type: str
            idp_single_sign_on_url:
                description:
                    - IDP single sign-on URL.
                type: str
            life:
                description:
                    - Length of the range of time when the assertion is valid (in minutes).
                type: int
            portal_url:
                description:
                    - SP portal URL.
                type: str
            role:
                description:
                    - SAML role.
                type: str
                choices:
                    - IDP
                    - SP
                    - identity_provider
                    - service_provider
            server_address:
                description:
                    - Server address.
                type: str
            service_providers:
                description:
                    - Authorized service providers.
                type: list
                suboptions:
                    assertion_attributes:
                        description:
                            - Customized SAML attributes to send along with assertion.
                        type: list
                        suboptions:
                            name:
                                description:
                                    - Name.
                                required: true
                                type: str
                            type:
                                description:
                                    - Type.
                                type: str
                                choices:
                                    - username
                                    - email
                                    - profile_name
                    idp_artifact_resolution_url:
                        description:
                            - IDP artifact resolution URL.
                        type: str
                    idp_entity_id:
                        description:
                            - IDP entity ID.
                        type: str
                    idp_single_logout_url:
                        description:
                            - IDP single logout URL.
                        type: str
                    idp_single_sign_on_url:
                        description:
                            - IDP single sign-on URL.
                        type: str
                    name:
                        description:
                            - Name.
                        required: true
                        type: str
                    prefix:
                        description:
                            - Prefix.
                        type: str
                    sp_artifact_resolution_url:
                        description:
                            - SP artifact resolution URL.
                        type: str
                    sp_binding_protocol:
                        description:
                            - SP binding protocol.
                        type: str
                        choices:
                            - post
                    sp_cert:
                        description:
                            - SP certificate name. Source certificate.remote.name.
                        type: str
                    sp_entity_id:
                        description:
                            - SP entity ID.
                        type: str
                    sp_portal_url:
                        description:
                            - SP portal URL.
                        type: str
                    sp_single_logout_url:
                        description:
                            - SP single logout URL.
                        type: str
                    sp_single_sign_on_url:
                        description:
                            - SP single sign-on URL.
                        type: str
            single_logout_url:
                description:
                    - SP single logout URL.
                type: str
            single_sign_on_url:
                description:
                    - SP single sign-on URL.
                type: str
            status:
                description:
                    - Enable/disable SAML authentication .
                type: str
                choices:
                    - enable
                    - disable
            tolerance:
                description:
                    - Tolerance to the range of time when the assertion is valid (in minutes).
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
  - name: Global settings for SAML authentication.
    fortios_system_saml:
      vdom:  "{{ vdom }}"
      system_saml:
        artifact_resolution_url: "<your_own_value>"
        binding_protocol: "post"
        cert: "<your_own_value> (source certificate.local.name)"
        default_login_page: "normal"
        default_profile: "<your_own_value> (source system.accprofile.name)"
        entity_id: "<your_own_value>"
        idp_artifact_resolution_url: "<your_own_value>"
        idp_cert: "<your_own_value> (source certificate.remote.name)"
        idp_entity_id: "<your_own_value>"
        idp_single_logout_url: "<your_own_value>"
        idp_single_sign_on_url: "<your_own_value>"
        life: "14"
        portal_url: "<your_own_value>"
        role: "IDP"
        server_address: "<your_own_value>"
        service_providers:
         -
            assertion_attributes:
             -
                name: "default_name_20"
                type: "username"
            idp_artifact_resolution_url: "<your_own_value>"
            idp_entity_id: "<your_own_value>"
            idp_single_logout_url: "<your_own_value>"
            idp_single_sign_on_url: "<your_own_value>"
            name: "default_name_26"
            prefix: "<your_own_value>"
            sp_artifact_resolution_url: "<your_own_value>"
            sp_binding_protocol: "post"
            sp_cert: "<your_own_value> (source certificate.remote.name)"
            sp_entity_id: "<your_own_value>"
            sp_portal_url: "<your_own_value>"
            sp_single_logout_url: "<your_own_value>"
            sp_single_sign_on_url: "<your_own_value>"
        single_logout_url: "<your_own_value>"
        single_sign_on_url: "<your_own_value>"
        status: "enable"
        tolerance: "38"

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


def filter_system_saml_data(json):
    option_list = ['artifact_resolution_url', 'binding_protocol', 'cert',
                   'default_login_page', 'default_profile', 'entity_id',
                   'idp_artifact_resolution_url', 'idp_cert', 'idp_entity_id',
                   'idp_single_logout_url', 'idp_single_sign_on_url', 'life',
                   'portal_url', 'role', 'server_address',
                   'service_providers', 'single_logout_url', 'single_sign_on_url',
                   'status', 'tolerance']
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


def system_saml(data, fos):
    vdom = data['vdom']
    system_saml_data = data['system_saml']
    filtered_data = underscore_to_hyphen(filter_system_saml_data(system_saml_data))

    return fos.set('system',
                   'saml',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_saml']:
        resp = system_saml(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_saml'))

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
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "disable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "entity_id": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "service_providers": {
            "type": "list",
            "children": {
                "sp_entity_id": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "assertion_attributes": {
                    "type": "list",
                    "children": {
                        "type": {
                            "type": "string",
                            "options": [
                                {
                                    "value": "username",
                                    "revisions": {
                                        "v6.2.0": True,
                                        "v6.2.3": True,
                                        "v6.4.0": True,
                                        "v6.4.1": True
                                    }
                                },
                                {
                                    "value": "email",
                                    "revisions": {
                                        "v6.2.0": True,
                                        "v6.2.3": True,
                                        "v6.4.0": True,
                                        "v6.4.1": True
                                    }
                                },
                                {
                                    "value": "profile-name",
                                    "revisions": {
                                        "v6.4.0": True,
                                        "v6.4.1": True
                                    }
                                }
                            ],
                            "revisions": {
                                "v6.2.0": True,
                                "v6.2.3": True,
                                "v6.4.0": True,
                                "v6.4.1": True
                            }
                        },
                        "name": {
                            "type": "string",
                            "revisions": {
                                "v6.2.0": True,
                                "v6.2.3": True,
                                "v6.4.0": True,
                                "v6.4.1": True
                            }
                        }
                    },
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "idp_artifact_resolution_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                "idp_single_logout_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "sp_artifact_resolution_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                "sp_cert": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "idp_entity_id": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "sp_binding_protocol": {
                    "type": "string",
                    "options": [
                        {
                            "value": "post",
                            "revisions": {
                                "v6.2.0": True,
                                "v6.2.3": True
                            }
                        }
                    ],
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                "prefix": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "sp_single_logout_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "sp_single_sign_on_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "idp_single_sign_on_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "sp_portal_url": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                "name": {
                    "type": "string",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            },
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "idp_artifact_resolution_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        },
        "idp_cert": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "idp_single_logout_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "tolerance": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "server_address": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "life": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "artifact_resolution_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        },
        "portal_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "single_sign_on_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "cert": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "role": {
            "type": "string",
            "options": [
                {
                    "value": "IDP",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": False,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "SP",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": False,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "identity-provider",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "service-provider",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "idp_entity_id": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "default_profile": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "default_login_page": {
            "type": "string",
            "options": [
                {
                    "value": "normal",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "sso",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "idp_single_sign_on_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "single_logout_url": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "binding_protocol": {
            "type": "string",
            "options": [
                {
                    "value": "post",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        }
    },
    "revisions": {
        "v6.2.0": True,
        "v6.2.3": True,
        "v6.4.0": True,
        "v6.4.1": True
    }
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "system_saml": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["system_saml"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["system_saml"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "system_saml")

        is_error, has_changed, result = fortios_system(module.params, fos)

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

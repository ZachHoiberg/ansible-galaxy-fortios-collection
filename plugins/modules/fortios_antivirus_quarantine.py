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
module: fortios_antivirus_quarantine
short_description: Configure quarantine options in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify antivirus feature and quarantine category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.8"
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

    antivirus_quarantine:
        description:
            - Configure quarantine options.
        default: null
        type: dict
        suboptions:
            agelimit:
                description:
                    - Age limit for quarantined files (0 - 479 hours, 0 means forever).
                type: int
            destination:
                description:
                    - Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or to delete them instead of quarantining them.
                type: str
                choices:
                    - NULL
                    - disk
                    - FortiAnalyzer
            drop_blocked:
                description:
                    - Do not quarantine dropped files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
            drop_heuristic:
                description:
                    - Do not quarantine files detected by heuristics found in sessions using the selected protocols. Dropped files are deleted instead of
                       being quarantined.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - https
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
            drop_infected:
                description:
                    - Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - https
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
            lowspace:
                description:
                    - Select the method for handling additional files when running low on disk space.
                type: str
                choices:
                    - drop_new
                    - ovrw_old
            maxfilesize:
                description:
                    - Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).
                type: int
            quarantine_quota:
                description:
                    - The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, depends on disk space).
                type: int
            store_blocked:
                description:
                    - Quarantine blocked files found in sessions using the selected protocols.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
            store_heuristic:
                description:
                    - Quarantine files detected by heuristics found in sessions using the selected protocols.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - https
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
            store_infected:
                description:
                    - Quarantine infected files found in sessions using the selected protocols.
                type: list
                choices:
                    - imap
                    - smtp
                    - pop3
                    - http
                    - ftp
                    - nntp
                    - imaps
                    - smtps
                    - pop3s
                    - https
                    - ftps
                    - mapi
                    - cifs
                    - mm1
                    - mm3
                    - mm4
                    - mm7
                    - ssh
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
  - name: Configure quarantine options.
    fortios_antivirus_quarantine:
      vdom:  "{{ vdom }}"
      antivirus_quarantine:
        agelimit: "3"
        destination: "NULL"
        drop_blocked: "imap"
        drop_heuristic: "imap"
        drop_infected: "imap"
        lowspace: "drop_new"
        maxfilesize: "9"
        quarantine_quota: "10"
        store_blocked: "imap"
        store_heuristic: "imap"
        store_infected: "imap"

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


def filter_antivirus_quarantine_data(json):
    option_list = ['agelimit', 'destination', 'drop_blocked',
                   'drop_heuristic', 'drop_infected', 'lowspace',
                   'maxfilesize', 'quarantine_quota', 'store_blocked',
                   'store_heuristic', 'store_infected']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_multilists_attributes(data):
    multilist_attrs = [[u'drop_infected'], [u'drop_heuristic'], [u'store_heuristic'], [u'store_infected'], [u'store_blocked'], [u'drop_blocked']]

    for attr in multilist_attrs:
        try:
            path = "data['" + "']['".join(elem for elem in attr) + "']"
            current_val = eval(path)
            flattened_val = ' '.join(elem for elem in current_val)
            exec(path + '= flattened_val')
        except BaseException:
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


def antivirus_quarantine(data, fos):
    vdom = data['vdom']
    antivirus_quarantine_data = data['antivirus_quarantine']
    antivirus_quarantine_data = flatten_multilists_attributes(antivirus_quarantine_data)
    filtered_data = underscore_to_hyphen(filter_antivirus_quarantine_data(antivirus_quarantine_data))

    return fos.set('antivirus',
                   'quarantine',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_antivirus(data, fos):

    if data['antivirus_quarantine']:
        resp = antivirus_quarantine(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('antivirus_quarantine'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "dict",
    "children": {
        "quarantine_quota": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "drop_infected": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "https",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "maxfilesize": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "agelimit": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "destination": {
            "type": "string",
            "options": [
                {
                    "value": "NULL",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "disk",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "FortiAnalyzer",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "drop_heuristic": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "https",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "store_heuristic": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "https",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "store_infected": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "https",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "store_blocked": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "lowspace": {
            "type": "string",
            "options": [
                {
                    "value": "drop-new",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ovrw-old",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "drop_blocked": {
            "multiple_values": True,
            "type": "list",
            "options": [
                {
                    "value": "imap",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "http",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "nntp",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "imaps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "smtps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "pop3s",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "ftps",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mapi",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "cifs",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "mm1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm4",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "mm7",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.0.0": True,
                        "v6.2.3": True,
                        "v6.4.0": False,
                        "v6.4.1": False
                    }
                },
                {
                    "value": "ssh",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        }
    },
    "revisions": {
        "v6.2.0": True,
        "v6.0.0": True,
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
        "antivirus_quarantine": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["antivirus_quarantine"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["antivirus_quarantine"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "antivirus_quarantine")

        is_error, has_changed, result = fortios_antivirus(module.params, fos)

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

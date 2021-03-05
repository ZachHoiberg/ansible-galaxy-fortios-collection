from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG

module_selectors_defs = {
    "update.switch-controller.managed-switch": {
        "url": "switch-controller/managed-switch/update",
        "params": {
            "admin": {
                "type": "string"
            },
            "fswname": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "update.system.ha-peer": {
        "url": "system/ha-peer/update",
        "params": {
            "priority": {
                "type": "int"
            },
            "serial_no": {
                "type": "string"
            },
            "hostname": {
                "type": "string"
            },
            "vcluster_id": {
                "type": "int"
            }
        }
    },
    "add-license.registration.vdom": {
        "url": "registration/vdom/add-license",
        "params": {
            "license": {
                "type": "string"
            }
        }
    },
    "geoip.geoip-query": {
        "url": "geoip/geoip-query/select",
        "params": {
            "ip_addresses": {
                "type": "array"
            }
        }
    },
    "clear-statistics.system.fortiguard": {
        "url": "system/fortiguard/clear-statistics",
        "params": {
        }
    },
    "disassociate.wifi.client": {
        "url": "wifi/client/disassociate",
        "params": {
            "mac": {
                "type": "string"
            }
        }
    },
    "upgrade.license.database": {
        "url": "license/database/upgrade",
        "params": {
            "file_content": {
                "type": "string"
            },
            "db_name": {
                "type": "string"
            }
        }
    },
    "clear_counters.firewall.policy": {
        "url": "firewall/policy/clear_counters",
        "params": {
            "policy": {
                "type": "int"
            }
        }
    },
    "test-availability.system.fortiguard": {
        "url": "system/fortiguard/test-availability",
        "params": {
            "protocol": {
                "type": "string"
            },
            "port": {
                "type": "int"
            },
            "service": {
                "type": "string"
            }
        }
    },
    "download.wifi.firmware": {
        "url": "wifi/firmware/download",
        "params": {
            "image_id": {
                "type": "string"
            }
        }
    },
    "provision.user.fortitoken": {
        "url": "user/fortitoken/provision",
        "params": {
            "tokens": {
                "type": "array"
            }
        }
    },
    "reset.firewall.per-ip-shaper": {
        "url": "firewall/per-ip-shaper/reset",
        "params": {
        }
    },
    "start.system.sniffer": {
        "url": "system/sniffer/start",
        "params": {
            "mkey": {
                "type": "int"
            }
        }
    },
    "update.system.modem": {
        "url": "system/modem/update",
        "params": {
        }
    },
    "update.web-ui.custom-language": {
        "url": "web-ui/custom-language/update",
        "params": {
            "file_content": {
                "type": "string"
            },
            "filename": {
                "type": "string"
            },
            "lang_comments": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            },
            "lang_name": {
                "type": "string"
            }
        }
    },
    "stop.wifi.vlan-probe": {
        "url": "wifi/vlan-probe/stop",
        "params": {
            "wtp": {
                "type": "string"
            },
            "ap_interface": {
                "type": "int"
            }
        }
    },
    "import.vpn-certificate.local": {
        "url": "vpn-certificate/local/import",
        "params": {
            "file_content": {
                "type": "string"
            },
            "certname": {
                "type": "string"
            },
            "key_file_content": {
                "type": "string"
            },
            "scope": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "type": {
                "type": "string"
            }
        }
    },
    "create.registration.forticare": {
        "url": "registration/forticare/create",
        "params": {
            "city": {
                "type": "string"
            },
            "first_name": {
                "type": "string"
            },
            "last_name": {
                "type": "string"
            },
            "industry_id": {
                "type": "int"
            },
            "orgsize_id": {
                "type": "int"
            },
            "title": {
                "type": "string"
            },
            "industry": {
                "type": "string"
            },
            "company": {
                "type": "string"
            },
            "reseller_id": {
                "type": "int"
            },
            "state_code": {
                "type": "string"
            },
            "phone": {
                "type": "string"
            },
            "state": {
                "type": "string"
            },
            "postal_code": {
                "type": "string"
            },
            "country_code": {
                "type": "int"
            },
            "address": {
                "type": "string"
            },
            "reseller_name": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    },
    "tunnel_reset_stats.vpn.ipsec": {
        "url": "vpn/ipsec/tunnel_reset_stats",
        "params": {
            "p1name": {
                "type": "string"
            }
        }
    },
    "register-device.registration.forticloud": {
        "url": "registration/forticloud/register-device",
        "params": {
            "country": {
                "type": "string"
            },
            "serial": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            },
            "reseller": {
                "type": "string"
            }
        }
    },
    "set_status.wifi.rogue_ap": {
        "url": "wifi/rogue_ap/set_status",
        "params": {
            "status": {
                "type": "string"
            },
            "ssid": {
                "type": "array"
            },
            "bssid": {
                "type": "array"
            }
        }
    },
    "email.user.guest": {
        "url": "user/guest/email",
        "params": {
            "group": {
                "type": "string"
            },
            "guest": {
                "type": "array"
            }
        }
    },
    "add.firewall.clearpass-address": {
        "url": "firewall/clearpass-address/add",
        "params": {
            "endpoint_ip": {
                "type": "array"
            },
            "spt": {
                "type": "string"
            }
        }
    },
    "import.vpn-certificate.crl": {
        "url": "vpn-certificate/crl/import",
        "params": {
            "file_content": {
                "type": "string"
            },
            "scope": {
                "type": "string"
            }
        }
    },
    "reset.webfilter.category-quota": {
        "url": "webfilter/category-quota/reset",
        "params": {
            "profile": {
                "type": "string"
            },
            "user": {
                "type": "string"
            }
        }
    },
    "upgrade.system.firmware": {
        "url": "system/firmware/upgrade",
        "params": {
            "file_content": {
                "type": "string"
            },
            "source": {
                "type": "string"
            },
            "ignore_invalid_signature": {
                "type": "boolean"
            },
            "format_partition": {
                "type": "boolean"
            },
            "filename": {
                "type": "string"
            }
        }
    },
    "tunnel_up.vpn.ipsec": {
        "url": "vpn/ipsec/tunnel_up",
        "params": {
            "p2name": {
                "type": "string"
            },
            "p2serial": {
                "type": "int"
            },
            "p1name": {
                "type": "string"
            }
        }
    },
    "factory-reset.switch-controller.managed-switch": {
        "url": "switch-controller/managed-switch/factory-reset",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "reset.wifi.euclid": {
        "url": "wifi/euclid/reset",
        "params": {
        }
    },
    "delete.log.local-report": {
        "url": "log/local-report/delete",
        "params": {
            "mkeys": {
                "type": "array"
            }
        }
    },
    "add-license.registration.forticare": {
        "url": "registration/forticare/add-license",
        "params": {
            "registration_code": {
                "type": "string"
            }
        }
    },
    "verify-cert.endpoint-control.ems": {
        "url": "endpoint-control/ems/verify-cert",
        "params": {
            "ems_name": {
                "type": "string"
            },
            "fingerprint": {
                "type": "string"
            }
        }
    },
    "cancel.fortiview.session": {
        "url": "fortiview/session/cancel",
        "params": {
            "device": {
                "type": "string"
            },
            "sessionid": {
                "type": "int"
            },
            "view_level": {
                "type": "string"
            },
            "report_by": {
                "type": "string"
            }
        }
    },
    "restart.wifi.managed_ap": {
        "url": "wifi/managed_ap/restart",
        "params": {
            "wtpname": {
                "type": "string"
            }
        }
    },
    "delete.webfilter.override": {
        "url": "webfilter/override/delete",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "stop.system.usb-log": {
        "url": "system/usb-log/stop",
        "params": {
        }
    },
    "close.firewall.session": {
        "url": "firewall/session/close",
        "params": {
            "daddr": {
                "type": "string"
            },
            "dport": {
                "type": "int"
            },
            "pro": {
                "type": "string"
            },
            "sport": {
                "type": "int"
            },
            "saddr": {
                "type": "string"
            }
        }
    },
    "reset.firewall.shaper": {
        "url": "firewall/shaper/reset",
        "params": {
        }
    },
    "clear_all.firewall.session": {
        "url": "firewall/session/clear_all",
        "params": {
        }
    },
    "clear_counters.firewall.acl": {
        "url": "firewall/acl/clear_counters",
        "params": {
            "policy": {
                "type": "int"
            }
        }
    },
    "revoke.system.dhcp": {
        "url": "system/dhcp/revoke",
        "params": {
            "ip": {
                "type": "array"
            }
        }
    },
    "start.system.fsck": {
        "url": "system/fsck/start",
        "params": {
        }
    },
    "change-vdom-mode.system.admin": {
        "url": "system/admin/change-vdom-mode",
        "params": {
            "vdom-mode": {
                "type": "string"
            }
        }
    },
    "refresh-server.user.fsso": {
        "url": "user/fsso/refresh-server",
        "params": {
        }
    },
    "trigger.system.security-rating": {
        "url": "system/security-rating/trigger",
        "params": {
            "report_types": {
                "type": "array"
            },
            "report_type": {
                "type": "string"
            }
        }
    },
    "webhook.system.automation-stitch": {
        "url": "system/automation-stitch/webhook",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "generate.vpn-certificate.csr": {
        "url": "vpn-certificate/csr/generate",
        "params": {
            "city": {
                "type": "string"
            },
            "orgunits": {
                "type": "array"
            },
            "countrycode": {
                "type": "string"
            },
            "scep_url": {
                "type": "string"
            },
            "curvename": {
                "type": "string"
            },
            "keytype": {
                "type": "string"
            },
            "certname": {
                "type": "string"
            },
            "scep_password": {
                "type": "string"
            },
            "state": {
                "type": "string"
            },
            "keysize": {
                "type": "int"
            },
            "scope": {
                "type": "string"
            },
            "sub_alt_name": {
                "type": "string"
            },
            "org": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            },
            "subject": {
                "type": "string"
            }
        }
    },
    "upload.system.vmlicense": {
        "url": "system/vmlicense/upload",
        "params": {
            "file_content": {
                "type": "string"
            }
        }
    },
    "add_users.user.banned": {
        "url": "user/banned/add_users",
        "params": {
            "ip_addresses": {
                "type": "array"
            },
            "expiry": {
                "type": "int"
            }
        }
    },
    "push.wifi.firmware": {
        "url": "wifi/firmware/push",
        "params": {
            "image_id": {
                "type": "string"
            },
            "serial": {
                "type": "string"
            }
        }
    },
    "eject.system.usb-device": {
        "url": "system/usb-device/eject",
        "params": {
        }
    },
    "reboot.system.os": {
        "url": "system/os/reboot",
        "params": {
            "event_log_message": {
                "type": "string"
            }
        }
    },
    "set.system.time": {
        "url": "system/time/set",
        "params": {
            "hour": {
                "type": "int"
            },
            "month": {
                "type": "int"
            },
            "second": {
                "type": "int"
            },
            "year": {
                "type": "int"
            },
            "day": {
                "type": "int"
            },
            "minute": {
                "type": "int"
            }
        }
    },
    "import.vpn-certificate.remote": {
        "url": "vpn-certificate/remote/import",
        "params": {
            "file_content": {
                "type": "string"
            },
            "scope": {
                "type": "string"
            }
        }
    },
    "push.switch-controller.fsw-firmware": {
        "url": "switch-controller/fsw-firmware/push",
        "params": {
            "image_id": {
                "type": "string"
            },
            "serial": {
                "type": "string"
            }
        }
    },
    "reset.wanopt.peer_stats": {
        "url": "wanopt/peer_stats/reset",
        "params": {
        }
    },
    "delete.vpn.ssl": {
        "url": "vpn/ssl/delete",
        "params": {
            "index": {
                "type": "int"
            },
            "type": {
                "type": "string"
            }
        }
    },
    "backup-action.system.fortimanager": {
        "url": "system/fortimanager/backup-action",
        "params": {
            "operation": {
                "type": "string"
            },
            "objects": {
                "type": "array"
            }
        }
    },
    "start.system.usb-log": {
        "url": "system/usb-log/start",
        "params": {
        }
    },
    "system.change-password": {
        "url": "system/change-password/select",
        "params": {
            "new_password": {
                "type": "string"
            },
            "old_password": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "tunnel_down.vpn.ipsec": {
        "url": "vpn/ipsec/tunnel_down",
        "params": {
            "p2name": {
                "type": "string"
            },
            "p2serial": {
                "type": "int"
            },
            "p1name": {
                "type": "string"
            }
        }
    },
    "clear_all.wifi.rogue_ap": {
        "url": "wifi/rogue_ap/clear_all",
        "params": {
        }
    },
    "import-seed.user.fortitoken": {
        "url": "user/fortitoken/import-seed",
        "params": {
            "file_content": {
                "type": "string"
            }
        }
    },
    "stop.system.sniffer": {
        "url": "system/sniffer/stop",
        "params": {
            "mkey": {
                "type": "int"
            }
        }
    },
    "logout.registration.forticloud": {
        "url": "registration/forticloud/logout",
        "params": {
        }
    },
    "restore.system.config": {
        "url": "system/config/restore",
        "params": {
            "config_id": {
                "type": "int"
            },
            "file_content": {
                "type": "string"
            },
            "usb_filename": {
                "type": "string"
            },
            "source": {
                "type": "string"
            },
            "scope": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "vdom": {
                "type": "string"
            }
        }
    },
    "import.vpn-certificate.ca": {
        "url": "vpn-certificate/ca/import",
        "params": {
            "file_content": {
                "type": "string"
            },
            "scope": {
                "type": "string"
            },
            "import_method": {
                "type": "string"
            },
            "scep_ca_id": {
                "type": "string"
            },
            "scep_url": {
                "type": "string"
            }
        }
    },
    "upload.switch-controller.fsw-firmware": {
        "url": "switch-controller/fsw-firmware/upload",
        "params": {
            "serials": {
                "type": "string"
            },
            "file_content": {
                "type": "string"
            }
        }
    },
    "test.user.tacacs-plus": {
        "url": "user/tacacs-plus/test",
        "params": {
            "ordinal": {
                "type": "string"
            },
            "source_ip": {
                "type": "string"
            },
            "server": {
                "type": "string"
            },
            "secret": {
                "type": "string"
            },
            "port": {
                "type": "int"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "upload.system.config-script": {
        "url": "system/config-script/upload",
        "params": {
            "file_content": {
                "type": "string"
            },
            "filename": {
                "type": "string"
            }
        }
    },
    "system.password-policy-conform": {
        "url": "system/password-policy-conform/select",
        "params": {
            "apply_to": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "old_password": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "sms.user.guest": {
        "url": "user/guest/sms",
        "params": {
            "group": {
                "type": "string"
            },
            "guest": {
                "type": "array"
            }
        }
    },
    "reset.wanopt.history": {
        "url": "wanopt/history/reset",
        "params": {
        }
    },
    "import-mobile.user.fortitoken": {
        "url": "user/fortitoken/import-mobile",
        "params": {
            "code": {
                "type": "string"
            }
        }
    },
    "download.switch-controller.fsw-firmware": {
        "url": "switch-controller/fsw-firmware/download",
        "params": {
            "image_id": {
                "type": "string"
            }
        }
    },
    "stop.wifi.spectrum": {
        "url": "wifi/spectrum/stop",
        "params": {
            "radio_id": {
                "type": "int"
            },
            "wtp_id": {
                "type": "string"
            }
        }
    },
    "login.registration.forticare": {
        "url": "registration/forticare/login",
        "params": {
            "reseller_name": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            },
            "reseller_id": {
                "type": "int"
            }
        }
    },
    "create.registration.forticloud": {
        "url": "registration/forticloud/create",
        "params": {
            "send_logs": {
                "type": "boolean"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    },
    "upload.wifi.firmware": {
        "url": "wifi/firmware/upload",
        "params": {
            "serials": {
                "type": "string"
            },
            "file_content": {
                "type": "string"
            }
        }
    },
    "start.wifi.spectrum": {
        "url": "wifi/spectrum/start",
        "params": {
            "radio_id": {
                "type": "int"
            },
            "channels": {
                "type": "array"
            },
            "duration": {
                "type": "int"
            },
            "wtp_id": {
                "type": "string"
            }
        }
    },
    "disconnect.system.modem": {
        "url": "system/modem/disconnect",
        "params": {
        }
    },
    "disconnect.system.ha-peer": {
        "url": "system/ha-peer/disconnect",
        "params": {
            "interface": {
                "type": "string"
            },
            "ip": {
                "type": "string"
            },
            "serial_no": {
                "type": "string"
            },
            "mask": {
                "type": "string"
            }
        }
    },
    "keep-alive.wifi.spectrum": {
        "url": "wifi/spectrum/keep-alive",
        "params": {
            "radio_id": {
                "type": "int"
            },
            "duration": {
                "type": "int"
            },
            "wtp_id": {
                "type": "string"
            }
        }
    },
    "reset.system.modem": {
        "url": "system/modem/reset",
        "params": {
        }
    },
    "activate.user.fortitoken": {
        "url": "user/fortitoken/activate",
        "params": {
            "tokens": {
                "type": "array"
            }
        }
    },
    "register-appliance.system.csf": {
        "url": "system/csf/register-appliance",
        "params": {
            "mgmt_ip": {
                "type": "string"
            },
            "mgmt_port": {
                "type": "int"
            },
            "hostname": {
                "type": "string"
            },
            "mgmt_url_parameters": {
                "type": "array"
            },
            "serial": {
                "type": "string"
            },
            "type": {
                "type": "string"
            }
        }
    },
    "start.wifi.vlan-probe": {
        "url": "wifi/vlan-probe/start",
        "params": {
            "wtp": {
                "type": "string"
            },
            "retries": {
                "type": "int"
            },
            "start_vlan_id": {
                "type": "int"
            },
            "end_vlan_id": {
                "type": "int"
            },
            "timeout": {
                "type": "int"
            },
            "ap_interface": {
                "type": "int"
            }
        }
    },
    "clear.system.sniffer": {
        "url": "system/sniffer/clear",
        "params": {
            "mkey": {
                "type": "int"
            }
        }
    },
    "reset.extender-controller.extender": {
        "url": "extender-controller/extender/reset",
        "params": {
            "id": {
                "type": "string"
            }
        }
    },
    "validate-gcp-key.system.sdn-connector": {
        "url": "system/sdn-connector/validate-gcp-key",
        "params": {
            "private-key": {
                "type": "string"
            }
        }
    },
    "restart.system.sniffer": {
        "url": "system/sniffer/restart",
        "params": {
            "mkey": {
                "type": "int"
            }
        }
    },
    "import.web-ui.language": {
        "url": "web-ui/language/import",
        "params": {
            "file_content": {
                "type": "string"
            }
        }
    },
    "import-trial.user.fortitoken": {
        "url": "user/fortitoken/import-trial",
        "params": {
        }
    },
    "dump.system.com-log": {
        "url": "system/com-log/dump",
        "params": {
        }
    },
    "diagnose.extender-controller.extender": {
        "url": "extender-controller/extender/diagnose",
        "params": {
            "cmd": {
                "type": "string"
            },
            "id": {
                "type": "string"
            }
        }
    },
    "update-comments.system.config-revision": {
        "url": "system/config-revision/update-comments",
        "params": {
            "config_id": {
                "type": "int"
            },
            "comments": {
                "type": "string"
            }
        }
    },
    "refresh.user.fortitoken": {
        "url": "user/fortitoken/refresh",
        "params": {
            "tokens": {
                "type": "array"
            }
        }
    },
    "reset.firewall.policy": {
        "url": "firewall/policy/reset",
        "params": {
        }
    },
    "clear_counters.firewall.acl6": {
        "url": "firewall/acl6/clear_counters",
        "params": {
            "policy": {
                "type": "int"
            }
        }
    },
    "reset.log.stats": {
        "url": "log/stats/reset",
        "params": {
        }
    },
    "revoke.system.dhcp6": {
        "url": "system/dhcp6/revoke",
        "params": {
            "ip": {
                "type": "array"
            }
        }
    },
    "login.registration.forticloud": {
        "url": "registration/forticloud/login",
        "params": {
            "send_logs": {
                "type": "boolean"
            },
            "domain": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    },
    "reset.wanopt.webcache": {
        "url": "wanopt/webcache/reset",
        "params": {
        }
    },
    "save.system.config-revision": {
        "url": "system/config-revision/save",
        "params": {
            "comments": {
                "type": "string"
            }
        }
    },
    "set_status.wifi.managed_ap": {
        "url": "wifi/managed_ap/set_status",
        "params": {
            "admin": {
                "type": "string"
            },
            "wtpname": {
                "type": "string"
            }
        }
    },
    "deauth.user.firewall": {
        "url": "user/firewall/deauth",
        "params": {
            "all": {
                "type": "boolean"
            },
            "users": {
                "type": "array"
            },
            "ip": {
                "type": "string"
            },
            "user_type": {
                "type": "string"
            },
            "id": {
                "type": "int"
            },
            "ip_version": {
                "type": "string"
            },
            "method": {
                "type": "string"
            }
        }
    },
    "upgrade.extender-controller.extender": {
        "url": "extender-controller/extender/upgrade",
        "params": {
            "file_content": {
                "type": "string"
            },
            "id": {
                "type": "string"
            }
        }
    },
    "delete.system.config-revision": {
        "url": "system/config-revision/delete",
        "params": {
            "config_ids": {
                "type": "array"
            }
        }
    },
    "clear_users.user.banned": {
        "url": "user/banned/clear_users",
        "params": {
            "ip_addresses": {
                "type": "array"
            }
        }
    },
    "send-activation.user.fortitoken": {
        "url": "user/fortitoken/send-activation",
        "params": {
            "token": {
                "type": "string"
            },
            "sms_phone": {
                "type": "string"
            },
            "method": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    },
    "reset.webcache.stats": {
        "url": "webcache/stats/reset",
        "params": {
        }
    },
    "clear_counters.firewall.proxy-policy": {
        "url": "firewall/proxy-policy/clear_counters",
        "params": {
            "policy": {
                "type": "int"
            }
        }
    },
    "utm.rating-lookup": {
        "url": "utm/rating-lookup/select",
        "params": {
            "url": {
                "type": "array"
            },
            "lang": {
                "type": "string"
            }
        }
    },
    "test.system.automation-stitch": {
        "url": "system/automation-stitch/test",
        "params": {
            "log": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "dhcp-renew.system.interface": {
        "url": "system/interface/dhcp-renew",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "migrate.registration.forticloud": {
        "url": "registration/forticloud/migrate",
        "params": {
            "password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    },
    "transfer.registration.forticare": {
        "url": "registration/forticare/transfer",
        "params": {
            "password": {
                "type": "string"
            },
            "old_password": {
                "type": "string"
            },
            "email": {
                "type": "string"
            },
            "old_email": {
                "type": "string"
            }
        }
    },
    "connect.wifi.network": {
        "url": "wifi/network/connect",
        "params": {
            "ssid": {
                "type": "string"
            }
        }
    },
    "test-connect.user.radius": {
        "url": "user/radius/test-connect",
        "params": {
            "ordinal": {
                "type": "string"
            },
            "server": {
                "type": "string"
            },
            "secret": {
                "type": "string"
            },
            "user": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "speed-test-trigger.system.interface": {
        "url": "system/interface/speed-test-trigger",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "generate-key.system.api-user": {
        "url": "system/api-user/generate-key",
        "params": {
            "api-user": {
                "type": "string"
            }
        }
    },
    "upload.wifi.region-image": {
        "url": "wifi/region-image/upload",
        "params": {
            "image_type": {
                "type": "string"
            },
            "file_content": {
                "type": "string"
            },
            "region_name": {
                "type": "string"
            }
        }
    },
    "poe-reset.switch-controller.managed-switch": {
        "url": "switch-controller/managed-switch/poe-reset",
        "params": {
            "port": {
                "type": "string"
            },
            "mkey": {
                "type": "string"
            }
        }
    },
    "run.system.config-script": {
        "url": "system/config-script/run",
        "params": {
            "remote_script": {
                "type": "string"
            }
        }
    },
    "clear_tunnel.vpn.ssl": {
        "url": "vpn/ssl/clear_tunnel",
        "params": {
        }
    },
    "add.nsx.service": {
        "url": "nsx/service/add",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "update.system.fortiguard": {
        "url": "system/fortiguard/update",
        "params": {
        }
    },
    "restart.switch-controller.managed-switch": {
        "url": "switch-controller/managed-switch/restart",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "delete.system.config-script": {
        "url": "system/config-script/delete",
        "params": {
            "id_list": {
                "type": "array"
            }
        }
    },
    "update.system.sdn-connector": {
        "url": "system/sdn-connector/update",
        "params": {
            "mkey": {
                "type": "string"
            }
        }
    },
    "config.system.fortimanager": {
        "url": "system/fortimanager/config",
        "params": {
            "unregister": {
                "type": "boolean"
            },
            "fortimanager_ip": {
                "type": "string"
            }
        }
    },
    "system.disconnect-admins": {
        "url": "system/disconnect-admins/select",
        "params": {
            "admins": {
                "type": "array"
            },
            "id": {
                "type": "int"
            },
            "method": {
                "type": "string"
            }
        }
    },
    "connect.system.modem": {
        "url": "system/modem/connect",
        "params": {
        }
    },
    "create.web-ui.custom-language": {
        "url": "web-ui/custom-language/create",
        "params": {
            "file_content": {
                "type": "string"
            },
            "lang_name": {
                "type": "string"
            },
            "lang_comments": {
                "type": "string"
            },
            "filename": {
                "type": "string"
            }
        }
    },
    "scan.wifi.network": {
        "url": "wifi/network/scan",
        "params": {
        }
    },
    "clear_counters.firewall.security-policy": {
        "url": "firewall/security-policy/clear_counters",
        "params": {
            "policy": {
                "type": "int"
            }
        }
    },
    "clear_all.user.banned": {
        "url": "user/banned/clear_all",
        "params": {
        }
    },
    "delete.firewall.clearpass-address": {
        "url": "firewall/clearpass-address/delete",
        "params": {
            "endpoint_ip": {
                "type": "array"
            },
            "spt": {
                "type": "string"
            }
        }
    },
    "shutdown.system.os": {
        "url": "system/os/shutdown",
        "params": {
            "event_log_message": {
                "type": "string"
            }
        }
    }
}


def is_successful_status(status):
    return status['status'] == "success" or \
        'http_method' in status and status['http_method'] == "DELETE" and status['http_status'] == 404


def validate_parameters(fos):
    #parameter validation will not block task, warning will be provided in case of parameters validation.
    mod_params = fos._module.params
    selector = mod_params['selector']
    params = mod_params['params']

    if params:
        for param_key, param_value in params.items():
            if type(param_value) not in [bool, int, str, list]:
                return False, {'message': 'value of param:%s must be atomic' % (param_key)}

    required_param_names = list(module_selectors_defs[selector]['params'].keys())
    provided_param_names = list(params.keys() if params else [])

    params_valid = True
    for param_name in required_param_names:
        if param_name not in provided_param_names:
            params_valid = False
            break
    if params_valid:
        for param_name in provided_param_names:
            if param_name not in required_param_names:
                params_valid = False
                break
    if not params_valid:
        param_summary = ['%s(%s)' % (param_name, param['type']) for param_name, param in module_selectors_defs[selector]['params'].items()]
        fos._module.warn("selector:%s expects params:%s" % (selector, str(param_summary)))
    return True, {}


def fortios_monitor_config(fos):
    valid, result = validate_parameters(fos)
    if not valid:
        return True, False, result

    params = fos._module.params

    selector = params['selector']
    selector_params = params['params']

    resp = fos.monitor_post(module_selectors_defs[selector]['url'], vdom=params['vdom'], data=selector_params)

    return not is_successful_status(resp), False, resp


def main():
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "enable_log": {"required": False, "type": bool},
        "params": {"required": False, "type": "dict" },
        "selector": {
            "required": True,
            "type": "str",
            "options": [
                "update.switch-controller.managed-switch",
                "update.system.ha-peer",
                "add-license.registration.vdom",
                "geoip.geoip-query",
                "clear-statistics.system.fortiguard",
                "disassociate.wifi.client",
                "upgrade.license.database",
                "clear_counters.firewall.policy",
                "test-availability.system.fortiguard",
                "download.wifi.firmware",
                "provision.user.fortitoken",
                "reset.firewall.per-ip-shaper",
                "start.system.sniffer",
                "update.system.modem",
                "update.web-ui.custom-language",
                "stop.wifi.vlan-probe",
                "import.vpn-certificate.local",
                "create.registration.forticare",
                "tunnel_reset_stats.vpn.ipsec",
                "register-device.registration.forticloud",
                "set_status.wifi.rogue_ap",
                "email.user.guest",
                "add.firewall.clearpass-address",
                "import.vpn-certificate.crl",
                "reset.webfilter.category-quota",
                "upgrade.system.firmware",
                "tunnel_up.vpn.ipsec",
                "factory-reset.switch-controller.managed-switch",
                "reset.wifi.euclid",
                "delete.log.local-report",
                "add-license.registration.forticare",
                "verify-cert.endpoint-control.ems",
                "cancel.fortiview.session",
                "restart.wifi.managed_ap",
                "delete.webfilter.override",
                "stop.system.usb-log",
                "close.firewall.session",
                "reset.firewall.shaper",
                "clear_all.firewall.session",
                "clear_counters.firewall.acl",
                "revoke.system.dhcp",
                "start.system.fsck",
                "change-vdom-mode.system.admin",
                "refresh-server.user.fsso",
                "trigger.system.security-rating",
                "webhook.system.automation-stitch",
                "generate.vpn-certificate.csr",
                "upload.system.vmlicense",
                "add_users.user.banned",
                "push.wifi.firmware",
                "eject.system.usb-device",
                "reboot.system.os",
                "set.system.time",
                "import.vpn-certificate.remote",
                "push.switch-controller.fsw-firmware",
                "reset.wanopt.peer_stats",
                "delete.vpn.ssl",
                "backup-action.system.fortimanager",
                "start.system.usb-log",
                "system.change-password",
                "tunnel_down.vpn.ipsec",
                "clear_all.wifi.rogue_ap",
                "import-seed.user.fortitoken",
                "stop.system.sniffer",
                "logout.registration.forticloud",
                "restore.system.config",
                "import.vpn-certificate.ca",
                "upload.switch-controller.fsw-firmware",
                "test.user.tacacs-plus",
                "upload.system.config-script",
                "system.password-policy-conform",
                "sms.user.guest",
                "reset.wanopt.history",
                "import-mobile.user.fortitoken",
                "download.switch-controller.fsw-firmware",
                "stop.wifi.spectrum",
                "login.registration.forticare",
                "create.registration.forticloud",
                "upload.wifi.firmware",
                "start.wifi.spectrum",
                "disconnect.system.modem",
                "disconnect.system.ha-peer",
                "keep-alive.wifi.spectrum",
                "reset.system.modem",
                "activate.user.fortitoken",
                "register-appliance.system.csf",
                "start.wifi.vlan-probe",
                "clear.system.sniffer",
                "reset.extender-controller.extender",
                "validate-gcp-key.system.sdn-connector",
                "restart.system.sniffer",
                "import.web-ui.language",
                "import-trial.user.fortitoken",
                "dump.system.com-log",
                "diagnose.extender-controller.extender",
                "update-comments.system.config-revision",
                "refresh.user.fortitoken",
                "reset.firewall.policy",
                "clear_counters.firewall.acl6",
                "reset.log.stats",
                "revoke.system.dhcp6",
                "login.registration.forticloud",
                "reset.wanopt.webcache",
                "save.system.config-revision",
                "set_status.wifi.managed_ap",
                "deauth.user.firewall",
                "upgrade.extender-controller.extender",
                "delete.system.config-revision",
                "clear_users.user.banned",
                "send-activation.user.fortitoken",
                "reset.webcache.stats",
                "clear_counters.firewall.proxy-policy",
                "utm.rating-lookup",
                "test.system.automation-stitch",
                "dhcp-renew.system.interface",
                "migrate.registration.forticloud",
                "transfer.registration.forticare",
                "connect.wifi.network",
                "test-connect.user.radius",
                "speed-test-trigger.system.interface",
                "generate-key.system.api-user",
                "upload.wifi.region-image",
                "poe-reset.switch-controller.managed-switch",
                "run.system.config-script",
                "clear_tunnel.vpn.ssl",
                "add.nsx.service",
                "update.system.fortiguard",
                "restart.switch-controller.managed-switch",
                "delete.system.config-script",
                "update.system.sdn-connector",
                "config.system.fortimanager",
                "system.disconnect-admins",
                "connect.system.modem",
                "create.web-ui.custom-language",
                "scan.wifi.network",
                "clear_counters.firewall.security-policy",
                "clear_all.user.banned",
                "delete.firewall.clearpass-address",
                "shutdown.system.os",
                ],
        }
    }

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        # Logging for fact module could be disabled/enabled.
        if 'enable_log' in module.params:
            connection.set_option('enable_log', module.params['enable_log'])
        else:
            connection.set_option('enable_log', False)

        fos = FortiOSHandler(connection, module)

        is_error, has_changed, result = fortios_monitor_config(fos)
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
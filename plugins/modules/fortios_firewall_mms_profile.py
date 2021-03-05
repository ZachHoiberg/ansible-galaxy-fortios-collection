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
module: fortios_firewall_mms_profile
short_description: Configure MMS profiles in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall feature and mms_profile category.
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
    firewall_mms_profile:
        description:
            - Configure MMS profiles.
        default: null
        type: dict
        suboptions:
            avnotificationtable:
                description:
                    - AntiVirus notification table ID. Source antivirus.notification.id.
                type: int
            bwordtable:
                description:
                    - MMS banned word table ID. Source webfilter.content.id.
                type: int
            carrier_endpoint_prefix:
                description:
                    - Enable/disable prefixing of end point values.
                type: str
                choices:
                    - enable
                    - disable
            carrier_endpoint_prefix_range_max:
                description:
                    - Maximum length of end point value that can be prefixed (1 - 48).
                type: int
            carrier_endpoint_prefix_range_min:
                description:
                    - Minimum end point length to be prefixed (1 - 48).
                type: int
            carrier_endpoint_prefix_string:
                description:
                    - String with which to prefix End point values.
                type: str
            carrierendpointbwltable:
                description:
                    - Carrier end point filter table ID. Source firewall.carrier-endpoint-bwl.id.
                type: int
            comment:
                description:
                    - Comment.
                type: str
            dupe:
                description:
                    - Duplicate configuration.
                type: list
                suboptions:
                    action1:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    action2:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    action3:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    block_time1:
                        description:
                            - Duration for which action takes effect (0 - 35791 min).
                        type: int
                    block_time2:
                        description:
                            - Duration for which action takes effect (0 - 35791 min).
                        type: int
                    block_time3:
                        description:
                            - Duration action takes effect (0 - 35791 min).
                        type: int
                    limit1:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    limit2:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    limit3:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    protocol:
                        description:
                            - Protocol.
                        required: true
                        type: str
                    status1:
                        description:
                            - Enable/disable status1 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    status2:
                        description:
                            - Enable/disable status2 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    status3:
                        description:
                            - Enable/disable status3 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    window1:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
                    window2:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
                    window3:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
            extended_utm_log:
                description:
                    - Enable/disable detailed UTM log messages.
                type: str
            flood:
                description:
                    - Flood configuration.
                type: list
                suboptions:
                    action1:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    action2:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    action3:
                        description:
                            - Action to take when threshold reached.
                        type: list
                        choices:
                            - block
                            - archive
                            - log
                            - archive-first
                            - alert-notif
                    block_time1:
                        description:
                            - Duration for which action takes effect (0 - 35791 min).
                        type: int
                    block_time2:
                        description:
                            - Duration for which action takes effect (0 - 35791 min).
                        type: int
                    block_time3:
                        description:
                            - Duration action takes effect (0 - 35791 min).
                        type: int
                    limit1:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    limit2:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    limit3:
                        description:
                            - Maximum number of messages allowed.
                        type: int
                    protocol:
                        description:
                            - Protocol.
                        required: true
                        type: str
                    status1:
                        description:
                            - Enable/disable status1 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    status2:
                        description:
                            - Enable/disable status2 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    status3:
                        description:
                            - Enable/disable status3 detection.
                        type: str
                        choices:
                            - enable
                            - disable
                    window1:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
                    window2:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
                    window3:
                        description:
                            - Window to count messages over (1 - 2880 min).
                        type: int
            mm1:
                description:
                    - MM1 options.
                type: list
                choices:
                    - avmonitor
                    - oversize
                    - quarantine
                    - scan
                    - bannedword
                    - chunkedbypass
                    - clientcomfort
                    - servercomfort
                    - carrier-endpoint-bwl
                    - remove-blocked
                    - mms-checksum
            mm1_addr_hdr:
                description:
                    - HTTP header field (for MM1) containing user address.
                type: str
            mm1_addr_source:
                description:
                    - Source for MM1 user address.
                type: str
                choices:
                    - http-header
                    - cookie
            mm1_convert_hex:
                description:
                    - Enable/disable converting user address from HEX string for MM1.
                type: str
                choices:
                    - enable
                    - disable
            mm1_outbreak_prevention:
                description:
                    - Enable FortiGuard Virus Outbreak Prevention service.
                type: str
                choices:
                    - disabled
                    - files
                    - full-archive
            mm1_retr_dupe:
                description:
                    - Enable/disable duplicate scanning of MM1 retr.
                type: str
                choices:
                    - enable
                    - disable
            mm1_retrieve_scan:
                description:
                    - Enable/disable scanning on MM1 retrieve configuration messages.
                type: str
                choices:
                    - enable
                    - disable
            mm1comfortamount:
                description:
                    - MM1 comfort amount (0 - 4294967295).
                type: int
            mm1comfortinterval:
                description:
                    - MM1 comfort interval (0 - 4294967295).
                type: int
            mm1oversizelimit:
                description:
                    - Maximum file size to scan (1 - 819200 kB).
                type: int
            mm3:
                description:
                    - MM3 options.
                type: list
                choices:
                    - avmonitor
                    - oversize
                    - quarantine
                    - scan
                    - bannedword
                    - fragmail
                    - splice
                    - carrier-endpoint-bwl
                    - remove-blocked
                    - mms-checksum
            mm3_outbreak_prevention:
                description:
                    - Enable FortiGuard Virus Outbreak Prevention service.
                type: str
                choices:
                    - disabled
                    - files
                    - full-archive
            mm3oversizelimit:
                description:
                    - Maximum file size to scan (1 - 819200 kB).
                type: int
            mm4:
                description:
                    - MM4 options.
                type: list
                choices:
                    - avmonitor
                    - oversize
                    - quarantine
                    - scan
                    - bannedword
                    - fragmail
                    - splice
                    - carrier-endpoint-bwl
                    - remove-blocked
                    - mms-checksum
            mm4_outbreak_prevention:
                description:
                    - Enable FortiGuard Virus Outbreak Prevention service.
                type: str
                choices:
                    - disabled
                    - files
                    - full-archive
            mm4oversizelimit:
                description:
                    - Maximum file size to scan (1 - 819200 kB).
                type: int
            mm7:
                description:
                    - MM7 options.
                type: list
                choices:
                    - avmonitor
                    - oversize
                    - quarantine
                    - scan
                    - bannedword
                    - chunkedbypass
                    - clientcomfort
                    - servercomfort
                    - carrier-endpoint-bwl
                    - remove-blocked
                    - mms-checksum
            mm7_addr_hdr:
                description:
                    - HTTP header field (for MM7) containing user address.
                type: str
            mm7_addr_source:
                description:
                    - Source for MM7 user address.
                type: str
                choices:
                    - http-header
                    - cookie
            mm7_convert_hex:
                description:
                    - Enable/disable conversion of user address from HEX string for MM7.
                type: str
                choices:
                    - enable
                    - disable
            mm7_outbreak_prevention:
                description:
                    - Enable FortiGuard Virus Outbreak Prevention service.
                type: str
                choices:
                    - disabled
                    - files
                    - full-archive
            mm7comfortamount:
                description:
                    - MM7 comfort amount (0 - 4294967295).
                type: int
            mm7comfortinterval:
                description:
                    - MM7 comfort interval (0 - 4294967295).
                type: int
            mm7oversizelimit:
                description:
                    - Maximum file size to scan (1 - 819200 kB).
                type: int
            mms_antispam_mass_log:
                description:
                    - Enable/disable logging for MMS antispam mass.
                type: str
                choices:
                    - enable
                    - disable
            mms_av_block_log:
                description:
                    - Enable/disable logging for MMS antivirus file blocking.
                type: str
                choices:
                    - enable
                    - disable
            mms_av_oversize_log:
                description:
                    - Enable/disable logging for MMS antivirus oversize file blocking.
                type: str
                choices:
                    - enable
                    - disable
            mms_av_virus_log:
                description:
                    - Enable/disable logging for MMS antivirus scanning.
                type: str
                choices:
                    - enable
                    - disable
            mms_carrier_endpoint_filter_log:
                description:
                    - Enable/disable logging for MMS end point filter blocking.
                type: str
                choices:
                    - enable
                    - disable
            mms_checksum_log:
                description:
                    - Enable/disable MMS content checksum logging.
                type: str
                choices:
                    - enable
                    - disable
            mms_checksum_table:
                description:
                    - MMS content checksum table ID. Source antivirus.mms-checksum.id.
                type: int
            mms_notification_log:
                description:
                    - Enable/disable logging for MMS notification messages.
                type: str
                choices:
                    - enable
                    - disable
            mms_web_content_log:
                description:
                    - Enable/disable logging for MMS web content blocking.
                type: str
                choices:
                    - enable
                    - disable
            mmsbwordthreshold:
                description:
                    - MMS banned word threshold.
                type: int
            name:
                description:
                    - Profile name.
                required: true
                type: str
            notif_msisdn:
                description:
                    - Notification for MSISDNs.
                type: list
                suboptions:
                    msisdn:
                        description:
                            - Recipient MSISDN.
                        required: true
                        type: str
                    threshold:
                        description:
                            - Thresholds on which this MSISDN will receive an alert.
                        type: str
                        choices:
                            - flood-thresh-1
                            - flood-thresh-2
                            - flood-thresh-3
                            - dupe-thresh-1
                            - dupe-thresh-2
                            - dupe-thresh-3
            notification:
                description:
                    - Notification configuration.
                type: list
                suboptions:
                    alert_int:
                        description:
                            - Alert notification send interval.
                        type: int
                    alert_int_mode:
                        description:
                            - Alert notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    alert_src_msisdn:
                        description:
                            - Specify from address for alert messages.
                        type: str
                    alert_status:
                        description:
                            - Alert notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    bword_int:
                        description:
                            - Banned word notification send interval.
                        type: int
                    bword_int_mode:
                        description:
                            - Banned word notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    bword_status:
                        description:
                            - Banned word notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    carrier_endpoint_bwl_int:
                        description:
                            - Carrier end point black/white list notification send interval.
                        type: int
                    carrier_endpoint_bwl_int_mode:
                        description:
                            - Carrier end point black/white list notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    carrier_endpoint_bwl_status:
                        description:
                            - Carrier end point black/white list notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    days_allowed:
                        description:
                            - Weekdays on which notification messages may be sent.
                        type: list
                        choices:
                            - sunday
                            - monday
                            - tuesday
                            - wednesday
                            - thursday
                            - friday
                            - saturday
                    detect_server:
                        description:
                            - Enable/disable automatic server address determination.
                        type: str
                        choices:
                            - enable
                            - disable
                    dupe_int:
                        description:
                            - Duplicate notification send interval.
                        type: int
                    dupe_int_mode:
                        description:
                            - Duplicate notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    dupe_status:
                        description:
                            - Duplicate notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    file_block_int:
                        description:
                            - File block notification send interval.
                        type: int
                    file_block_int_mode:
                        description:
                            - File block notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    file_block_status:
                        description:
                            - File block notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    flood_int:
                        description:
                            - Flood notification send interval.
                        type: int
                    flood_int_mode:
                        description:
                            - Flood notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    flood_status:
                        description:
                            - Flood notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    from_in_header:
                        description:
                            - Enable/disable insertion of from address in HTTP header.
                        type: str
                        choices:
                            - enable
                            - disable
                    mms_checksum_int:
                        description:
                            - MMS checksum notification send interval.
                        type: int
                    mms_checksum_int_mode:
                        description:
                            - MMS checksum notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    mms_checksum_status:
                        description:
                            - MMS checksum notification status.
                        type: str
                        choices:
                            - enable
                            - disable
                    mmsc_hostname:
                        description:
                            - Host name or IP address of the MMSC.
                        type: str
                    mmsc_password:
                        description:
                            - Password required for authentication with the MMSC.
                        type: str
                    mmsc_port:
                        description:
                            - Port used on the MMSC for sending MMS messages (1 - 65535).
                        type: int
                    mmsc_url:
                        description:
                            - URL used on the MMSC for sending MMS messages.
                        type: str
                    mmsc_username:
                        description:
                            - User name required for authentication with the MMSC.
                        type: str
                    msg_protocol:
                        description:
                            - Protocol to use for sending notification messages.
                        type: str
                        choices:
                            - mm1
                            - mm3
                            - mm4
                            - mm7
                    msg_type:
                        description:
                            - MM7 message type.
                        type: str
                        choices:
                            - submit-req
                            - deliver-req
                    protocol:
                        description:
                            - Protocol.
                        required: true
                        type: str
                    rate_limit:
                        description:
                            - Rate limit for sending notification messages (0 - 250).
                        type: int
                    tod_window_duration:
                        description:
                            - Time of day window duration.
                        type: str
                    tod_window_end:
                        description:
                            - Obsolete.
                        type: str
                    tod_window_start:
                        description:
                            - Time of day window start.
                        type: str
                    user_domain:
                        description:
                            - Domain name to which the user addresses belong.
                        type: str
                    vas_id:
                        description:
                            - VAS identifier.
                        type: str
                    vasp_id:
                        description:
                            - VASP identifier.
                        type: str
                    virus_int:
                        description:
                            - Virus notification send interval.
                        type: int
                    virus_int_mode:
                        description:
                            - Virus notification interval mode.
                        type: str
                        choices:
                            - hours
                            - minutes
                    virus_status:
                        description:
                            - Virus notification status.
                        type: str
                        choices:
                            - enable
                            - disable
            outbreak_prevention:
                description:
                    - Configure Virus Outbreak Prevention settings.
                type: dict
                suboptions:
                    external_blocklist:
                        description:
                            - Enable/disable external malware blocklist.
                        type: str
                        choices:
                            - disable
                            - enable
                    ftgd_service:
                        description:
                            - Enable/disable FortiGuard Virus outbreak prevention service.
                        type: str
                        choices:
                            - disable
                            - enable
            remove_blocked_const_length:
                description:
                    - Enable/disable MMS replacement of blocked file constant length.
                type: str
                choices:
                    - enable
                    - disable
            replacemsg_group:
                description:
                    - Replacement message group. Source system.replacemsg-group.name.
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
  - name: Configure MMS profiles.
    fortios_firewall_mms_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_mms_profile:
        avnotificationtable: "3 (source antivirus.notification.id)"
        bwordtable: "4 (source webfilter.content.id)"
        carrier_endpoint_prefix: "enable"
        carrier_endpoint_prefix_range_max: "6"
        carrier_endpoint_prefix_range_min: "7"
        carrier_endpoint_prefix_string: "<your_own_value>"
        carrierendpointbwltable: "9 (source firewall.carrier-endpoint-bwl.id)"
        comment: "Comment."
        dupe:
         -
            action1: "block"
            action2: "block"
            action3: "block"
            block_time1: "15"
            block_time2: "16"
            block_time3: "17"
            limit1: "18"
            limit2: "19"
            limit3: "20"
            protocol: "<your_own_value>"
            status1: "enable"
            status2: "enable"
            status3: "enable"
            window1: "25"
            window2: "26"
            window3: "27"
        extended_utm_log: "<your_own_value>"
        flood:
         -
            action1: "block"
            action2: "block"
            action3: "block"
            block_time1: "33"
            block_time2: "34"
            block_time3: "35"
            limit1: "36"
            limit2: "37"
            limit3: "38"
            protocol: "<your_own_value>"
            status1: "enable"
            status2: "enable"
            status3: "enable"
            window1: "43"
            window2: "44"
            window3: "45"
        mm1: "avmonitor"
        mm1_addr_hdr: "<your_own_value>"
        mm1_addr_source: "http-header"
        mm1_convert_hex: "enable"
        mm1_outbreak_prevention: "disabled"
        mm1_retr_dupe: "enable"
        mm1_retrieve_scan: "enable"
        mm1comfortamount: "53"
        mm1comfortinterval: "54"
        mm1oversizelimit: "55"
        mm3: "avmonitor"
        mm3_outbreak_prevention: "disabled"
        mm3oversizelimit: "58"
        mm4: "avmonitor"
        mm4_outbreak_prevention: "disabled"
        mm4oversizelimit: "61"
        mm7: "avmonitor"
        mm7_addr_hdr: "<your_own_value>"
        mm7_addr_source: "http-header"
        mm7_convert_hex: "enable"
        mm7_outbreak_prevention: "disabled"
        mm7comfortamount: "67"
        mm7comfortinterval: "68"
        mm7oversizelimit: "69"
        mms_antispam_mass_log: "enable"
        mms_av_block_log: "enable"
        mms_av_oversize_log: "enable"
        mms_av_virus_log: "enable"
        mms_carrier_endpoint_filter_log: "enable"
        mms_checksum_log: "enable"
        mms_checksum_table: "76 (source antivirus.mms-checksum.id)"
        mms_notification_log: "enable"
        mms_web_content_log: "enable"
        mmsbwordthreshold: "79"
        name: "default_name_80"
        notif_msisdn:
         -
            msisdn: "<your_own_value>"
            threshold: "flood-thresh-1"
        notification:
         -
            alert_int: "85"
            alert_int_mode: "hours"
            alert_src_msisdn: "<your_own_value>"
            alert_status: "enable"
            bword_int: "89"
            bword_int_mode: "hours"
            bword_status: "enable"
            carrier_endpoint_bwl_int: "92"
            carrier_endpoint_bwl_int_mode: "hours"
            carrier_endpoint_bwl_status: "enable"
            days_allowed: "sunday"
            detect_server: "enable"
            dupe_int: "97"
            dupe_int_mode: "hours"
            dupe_status: "enable"
            file_block_int: "100"
            file_block_int_mode: "hours"
            file_block_status: "enable"
            flood_int: "103"
            flood_int_mode: "hours"
            flood_status: "enable"
            from_in_header: "enable"
            mms_checksum_int: "107"
            mms_checksum_int_mode: "hours"
            mms_checksum_status: "enable"
            mmsc_hostname: "myhostname"
            mmsc_password: "<your_own_value>"
            mmsc_port: "112"
            mmsc_url: "<your_own_value>"
            mmsc_username: "<your_own_value>"
            msg_protocol: "mm1"
            msg_type: "submit-req"
            protocol: "<your_own_value>"
            rate_limit: "118"
            tod_window_duration: "<your_own_value>"
            tod_window_end: "<your_own_value>"
            tod_window_start: "<your_own_value>"
            user_domain: "<your_own_value>"
            vas_id: "<your_own_value>"
            vasp_id: "<your_own_value>"
            virus_int: "125"
            virus_int_mode: "hours"
            virus_status: "enable"
        outbreak_prevention:
            external_blocklist: "disable"
            ftgd_service: "disable"
        remove_blocked_const_length: "enable"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"

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


def filter_firewall_mms_profile_data(json):
    option_list = ['avnotificationtable', 'bwordtable', 'carrier_endpoint_prefix',
                   'carrier_endpoint_prefix_range_max', 'carrier_endpoint_prefix_range_min', 'carrier_endpoint_prefix_string',
                   'carrierendpointbwltable', 'comment', 'dupe',
                   'extended_utm_log', 'flood', 'mm1',
                   'mm1_addr_hdr', 'mm1_addr_source', 'mm1_convert_hex',
                   'mm1_outbreak_prevention', 'mm1_retr_dupe', 'mm1_retrieve_scan',
                   'mm1comfortamount', 'mm1comfortinterval', 'mm1oversizelimit',
                   'mm3', 'mm3_outbreak_prevention', 'mm3oversizelimit',
                   'mm4', 'mm4_outbreak_prevention', 'mm4oversizelimit',
                   'mm7', 'mm7_addr_hdr', 'mm7_addr_source',
                   'mm7_convert_hex', 'mm7_outbreak_prevention', 'mm7comfortamount',
                   'mm7comfortinterval', 'mm7oversizelimit', 'mms_antispam_mass_log',
                   'mms_av_block_log', 'mms_av_oversize_log', 'mms_av_virus_log',
                   'mms_carrier_endpoint_filter_log', 'mms_checksum_log', 'mms_checksum_table',
                   'mms_notification_log', 'mms_web_content_log', 'mmsbwordthreshold',
                   'name', 'notif_msisdn', 'notification',
                   'outbreak_prevention', 'remove_blocked_const_length', 'replacemsg_group' ]
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary

def flatten_multilists_attributes(data):
    multilist_attrs = [[u'mm4'], [u'mm7'], [u'mm1'], [u'mm3'], [u'dupe', u'action1'], [u'dupe', u'action3'], [u'dupe', u'action2'], [u'notification',
       u'days_allowed'], [u'flood', u'action1'], [u'flood', u'action3'], [u'flood', u'action2'], [u'notif_msisdn', u'threshold']]

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

def firewall_mms_profile(data, fos):
    vdom = data['vdom']
    
    state = data['state']
    
    firewall_mms_profile_data = data['firewall_mms_profile']
    firewall_mms_profile_data = flatten_multilists_attributes(firewall_mms_profile_data)
    filtered_data = underscore_to_hyphen(filter_firewall_mms_profile_data(firewall_mms_profile_data))

    
    if state == "present" or state == True:
        return fos.set('firewall',
                       'mms-profile',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall',
                          'mms-profile',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')
    

def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404




def fortios_firewall(data, fos):

    if data['firewall_mms_profile']:
        resp = firewall_mms_profile(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_mms_profile'))

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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_antispam_mass_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_convert_hex": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm4": {
            "multiple_values": True, 
            "type": "list", 
            "options": [
                {
                    "value": "avmonitor", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "oversize", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "quarantine", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "scan", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "bannedword", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "fragmail", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "splice", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "carrier-endpoint-bwl", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "remove-blocked", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "mms-checksum", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7": {
            "multiple_values": True, 
            "type": "list", 
            "options": [
                {
                    "value": "avmonitor", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "oversize", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "quarantine", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "scan", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "bannedword", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "chunkedbypass", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "clientcomfort", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "servercomfort", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "carrier-endpoint-bwl", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "remove-blocked", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "mms-checksum", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mmsbwordthreshold": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1": {
            "multiple_values": True, 
            "type": "list", 
            "options": [
                {
                    "value": "avmonitor", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "oversize", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "quarantine", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "scan", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "bannedword", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "chunkedbypass", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "clientcomfort", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "servercomfort", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "carrier-endpoint-bwl", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "remove-blocked", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "mms-checksum", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm3": {
            "multiple_values": True, 
            "type": "list", 
            "options": [
                {
                    "value": "avmonitor", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "oversize", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "quarantine", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "scan", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "bannedword", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "fragmail", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "splice", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "carrier-endpoint-bwl", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "remove-blocked", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "mms-checksum", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "dupe": {
            "type": "list", 
            "children": {
                "status1": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "status3": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "status2": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action1": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action3": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action2": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "protocol": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm4oversizelimit": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "replacemsg_group": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_checksum_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7_outbreak_prevention": {
            "type": "string", 
            "options": [
                {
                    "value": "disabled", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "files", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "full-archive", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "bwordtable": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "notification": {
            "type": "list", 
            "children": {
                "from_in_header": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "bword_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "protocol": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "msg_type": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "submit-req", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "deliver-req", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "carrier_endpoint_bwl_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "vas_id": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "file_block_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "msg_protocol": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "mm1", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "mm3", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "mm4", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "mm7", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "carrier_endpoint_bwl_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "flood_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "flood_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "alert_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "tod_window_end": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "flood_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "file_block_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mmsc_username": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "virus_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mms_checksum_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mmsc_hostname": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "dupe_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mmsc_port": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "bword_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "alert_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "dupe_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mms_checksum_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "virus_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "alert_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "alert_src_msisdn": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "days_allowed": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "sunday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "monday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "tuesday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "wednesday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "thursday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "friday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "saturday", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "vasp_id": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "detect_server": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "tod_window_start": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mmsc_url": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mms_checksum_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "tod_window_duration": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "rate_limit": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "virus_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "mmsc_password": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "file_block_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "dupe_int_mode": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "hours", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "minutes", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "bword_status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "carrier_endpoint_bwl_int": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "user_domain": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7_convert_hex": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm3oversizelimit": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7comfortinterval": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1oversizelimit": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "flood": {
            "type": "list", 
            "children": {
                "status1": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "status3": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "status2": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "window1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action1": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action3": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action2": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "log", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "archive-first", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "alert-notif", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time2": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "block_time3": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "protocol": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "limit1": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7_addr_hdr": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_av_virus_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_av_oversize_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "carrier_endpoint_prefix_range_min": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_carrier_endpoint_filter_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7comfortamount": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "notif_msisdn": {
            "type": "list", 
            "children": {
                "msisdn": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "threshold": {
                    "multiple_values": True, 
                    "type": "list", 
                    "options": [
                        {
                            "value": "flood-thresh-1", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "flood-thresh-2", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "flood-thresh-3", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "dupe-thresh-1", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "dupe-thresh-2", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "dupe-thresh-3", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_web_content_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_retrieve_scan": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_retr_dupe": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1comfortamount": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7_addr_source": {
            "type": "string", 
            "options": [
                {
                    "value": "http-header", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "cookie", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm7oversizelimit": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "avnotificationtable": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_checksum_table": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "outbreak_prevention": {
            "type": "dict", 
            "children": {
                "external_blocklist": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True
                            }
                        }, 
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True
                    }
                }, 
                "ftgd_service": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True
                            }
                        }, 
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True
                    }
                }
            }, 
            "revisions": {
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True
            }
        }, 
        "mm1comfortinterval": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "remove_blocked_const_length": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "carrierendpointbwltable": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_addr_hdr": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "extended_utm_log": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_av_block_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "carrier_endpoint_prefix_range_max": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm3_outbreak_prevention": {
            "type": "string", 
            "options": [
                {
                    "value": "disabled", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "files", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "full-archive", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm4_outbreak_prevention": {
            "type": "string", 
            "options": [
                {
                    "value": "disabled", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "files", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "full-archive", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_outbreak_prevention": {
            "type": "string", 
            "options": [
                {
                    "value": "disabled", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "files", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "full-archive", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mms_notification_log": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "carrier_endpoint_prefix": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "mm1_addr_source": {
            "type": "string", 
            "options": [
                {
                    "value": "http-header", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "cookie", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v6.0.5": True, 
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
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "carrier_endpoint_prefix_string": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v6.0.5": True, 
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
        "firewall_mms_profile": {
            "required": False, "type": "dict", "default": None,
            "options": { 
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["firewall_mms_profile"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["firewall_mms_profile"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "firewall_mms_profile")
        
        is_error, has_changed, result = fortios_firewall(module.params, fos)
        
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
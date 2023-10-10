# Get Spanning Tree Statistics

**URL** : `/uiGetSpanningTreeStats/`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Response** : JSON

```json
{
    "bpdu_filtered_ports": [
    ],
    "bpdu_protected_ports": [
    ],
    "enabled": Boolean,
    "loop_guard_ports": [
    ],
    "loop_inc_ports": [
    ],
    "mstp_details": {
        "cfg_digest": String,
        "cfg_name": String,
        "cfg_revision": String,
        "change_count": String,
        "time_change": String
    },
    "root_guard_ports": [
    ],
    "root_inc_ports": [
    ],
    "tcn_guard_ports": [
    ],
    "type": String
}


```
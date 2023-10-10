# Get System Status

**URL** : `/uiGetStatus/`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Response** : JSON

```json
{
    "success": 1,
    "system_status": {
        "member_data": [
            {
                "member": Integer,
                "poe": {
                    "denied": Integer,
                    "faults": Integer,
                    "isPoe": Boolean
                },
                "storage": {
                    "critical": Integer,
                    "current": Integer,
                    "details": [
                        {
                            "name": String,
                            "usage": Integer
                        },
                        {
                            "name": String,
                            "usage": Integer
                        }
                    ],
                    "warning": Integer
                }
            }
        ],
        "session_timeout": Integer
    }
}
```
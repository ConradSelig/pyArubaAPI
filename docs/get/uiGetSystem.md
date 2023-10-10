# Get System Details

**URL** : `/uiGetSystem/`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Response** : JSON

```json
{
    "system_static": {
        "boot_image": String,
        "contact": String,
        "isPoe": Boolean,
        "location": String,
        "mac": String,
        "primary_software": String,
        "product": String,
        "rom": String,
        "secondary_software": String,
        "serial": String,
        "system_name": String,
        "system_time": Integer,
        "timezone": Integer,
        "uptime": String
    }
}
```
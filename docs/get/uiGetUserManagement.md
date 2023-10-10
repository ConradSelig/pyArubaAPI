# Get System Details

**URL** : `/uiGetUserManagement/`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Response** : JSON

```json
{
    "centralmgmt": Boolean,
    "session": {
        "auth_level": Integer,
        "logged_in": Boolean,
        "name": String,
        "role": String
    },
    "supportmode": Boolean
}
```
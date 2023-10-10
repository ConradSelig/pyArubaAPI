# Get System Users

**URL** : `/uiGetUserRole/`

**Method** : `GET`

**Auth required** : YES

## Success Response

**Code** : `200 OK`

**Response** : JSON

```json
{
    "roles": [
        {
            "configured": Boolean,
            "name": String
        }
    ]
}
```
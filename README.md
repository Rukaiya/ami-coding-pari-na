# ami-coding-pari-na
web application with khoj the search page and api endpoint to filter userwise entry
## Setup Guideline
___
- create a virtual environment using `pipenv shell`
- install dependencies
- create an .env file and provide followings:
    - SECRET_KEY='YOUR_SECRET_KEY_HERE'
    - DB_NAME='YOUR_DATABASE_NAME_HERE'
    - DB_USER='YOUR_DATABASE_USERNAME_HERE'
    - DB_PASSWORD='YOUR_DATABASE_PASSWORD_HERE'
    - DB_HOST=localhost
    - DB_PORT=5432
- make migration
- create superuser

## Api Documentation
___
`BASE_URL: http://127.0.0.1:8000`

### Get User Access Token

* **URL :** `BASE_URL + /api/token`

* **Method :** `POST`

* **URL Params :**

```json
{
    "username": "USERNAME",
    "password": "PASSWORD"
}
```
* **Success Response**
 * **Code :**`200`
 * **Content :**
```json
{
    "refresh": "REFRESH_TOKEN",
    "access": "ACCESS_TOKEN"
}
```
### Get User Refresh Token

`BASE_URL: http://127.0.0.1:8000`

* **URL :** `BASE_URL + /api/token/refresh`

* **Method :** `POST`

* **URL Params :**

```json
{
    "refresh": "REFRESH_TOKEN"
}
```
* **Success Response**
 * **Code :**`200`
 * **Content :**
```json
{
    "refresh": "REFRESH_TOKEN",
    "access": "ACCESS_TOKEN"
}
```

### Get User's Input Value
___
`BASE_URL: http://127.0.0.1:8000`

* **URL :** `BASE_URL + /api/user-info`

* **Method :** `GET`

* **URL Params :**

```json
{
    "user_id": 1,
    "start_datetime": "2012-01-01 00:00:00",
    "end_datetime": "2013-01-01 01:00:00"
}
```
* **Success Response**
 * **Code :**`200`
 * **Content :**
```json
{
    "status": "success",
    "user_id": "1",
    "payload": [
        {
            "timestamp": "2022-11-11 20:17:25.134658",
            "input_values": "[500000, 100, 1]"
        },
        {
            "timestamp": "2022-11-11 20:17:38.325713",
            "input_values": "[20, 6, 1]"
        },
        {
            "timestamp": "2022-11-11 20:32:48.574615",
            "input_values": "[500, 2, 1]"
        }
    ]
}
```
* **Success Response**
 * **Code :**`200`
 * **Content :**
```json
{
    "status": "success",
    "user_id": "5",
    "payload": "User not Found"
}
```

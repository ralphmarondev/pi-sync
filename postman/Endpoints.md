# Endpoints for PiSync

## Room [door]

Endpoints for operations related to rooms.

### register new room

```
door/new/

{
    "name": "A14"
}
```

### list of doors

```
doors/
```

### Delete door by id

```
door/delete/4/
```

### Doors registered to a username

```
doors/username/ralphmaron/
```

## Tenants | Users

Endpoints for operations related to rooms.

### register

```
register/

{
    "username": "ralphmaron",
    "first_name": "Ralph Maron",
    "last_name": "Eda",
    "password": "iscute",
    "hint_password": "Look at the mirror :)",
    "gender": "Male",
    "registered_doors": [1]
}
```

### login

```
login/

{
    "username": "ralphmaron",
    "password": "iscute"
}
```

### password hint

```
user/password-hint/ralphmaron/
```

### User details by id

```
user/1
```

### Users list

```
users/
```

### User details by username

```
user/username/ralphmaron/
```

## Door status [opening or closing of door]

### Opening door by id

```
door/open/1/
```

### Close door by id

```
door/close/1/
```

### Door status [if it is open or close0]

```
door/status/1
```

## History

### List of histories of all rooms

```
history/
```

### History list of a certain room by id

```
history/room/1/
```

# Stalker

Maintain a list of users in your office/house using ARP tables to resolve IP and MAC addresses.


## Inspiration

Zach Holman's [play](https://github.com/holman/play) mentions how Github work out who is in the office which I'm trying to replicate here with interchangeable backends.


## API

Stalker provides a JSON REST API allowing you to query the current user list. A `GET` request to `/` will return a list of hosts like so:

    [
        {
            "mac": "00:00:00:00:00:00",
            "ip": "192.168.0.0"
        }
    ]


## ARP Backends

Since all routers display their ARP tables at different urls, and may even provide an API, stalker provides a backend architecture.

Set the `BACKEND` variable in `settings.py` to the python path of you backend class:

    BACKEND = 'backends.my_router.Backend'


flask, backed with redis, fronted with gunicorn, nginx.


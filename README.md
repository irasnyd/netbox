NetBox on Docker
================

This is a Docker-ized container of the excellent
[DigitalOcean NetBox](https://github.com/digitalocean/netbox) web application.

[![](https://images.microbadger.com/badges/image/irasnyd/netbox.svg)](https://microbadger.com/images/irasnyd/netbox "Get your own image badge on microbadger.com")

Instructions
============

A simple all-in-one [Docker Compose](https://docs.docker.com/compose/) file is
provided to make testing this software as simple as possible. In order to use
it, simply run:

    docker-compose up -d

If you need a more complex setup, you should customize the environment
variables that you need for your deployment.

Environment Variables
=====================

These are available for you to customize as needed.

- **DB_NAME**: The database name. Defaults to `netbox`.
- **DB_USER**: The database user. Defaults to `netbox`.
- **DB_PASS**: The database password. Defaults to `netbox`.
- **DB_HOST**: The database server hostname. Defaults to `localhost`.
- **DB_PORT**: The database server port. Defaults to `5432`.
- **SECRET_KEY**: Secret key for verifying cookie session data integrity. Defaults to a random alphanumeric string.
- **EMAIL_SERVER**: Email server hostname. Defaults to `localhost`.
- **EMAIL_PORT**: Email server port. Defaults to `25`.
- **EMAIL_USERNAME**: Email username.
- **EMAIL_PASSWORD**: Email password.
- **EMAIL_TIMEOUT**: Email timeout. Defaults to `10`.
- **EMAIL_FROM**: Email "From" address.
- **LOGIN_REQUIRED**: Require login to access any information. Defaults to `False` (read only access allowed).
- **MAINTENANCE_MODE**: Display a maintenance mode banner. Defaults to `False`.
- **DEVICE_USERNAME**: Username that netbox will use to access live devices.
- **DEVICE_PASSWORD**: Password that netbox will use to access live devices.
- **PAGINATE_COUNT**: How many objects to display per page in lists. Defaults to `50`.

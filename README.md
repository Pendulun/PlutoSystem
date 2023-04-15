# PlutoSystem

See [docs/README.md](/docs/README.md) for information on how the system should
work.

## Building and running

### Pre-requisites

We use `docker`, `docker-compose` and the PG client `psql` to start the
system. Please install these tools properly before proceeding.

The Makefile commands assume a Linux or MacOS environment. Please use a virtual
machine in case that is not your environment.

### Build commands

#### Start

To build and run the system with a test database, run:

```shell
make start
```

#### Restart

To restart the system, run

```shell
make restart
```

#### Stop

To stop the system, run

```shell
make stop
```

## Testing

After the system is running locally, do whatever you want with it. For example,
to connect to the test database, run

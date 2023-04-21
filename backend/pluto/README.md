# Pluto backend

The Pluto backend is written in python.

## Installing

### Debian-based linux

```shell
sudo apt-get install python3.10-dev
python3.10 -m venv venv
source venv/bin/activate
poetry install
```

## Testing

The `check` make rule runs linting and tests (including integration tests):

```shell
make check
```

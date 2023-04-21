from uuid import uuid4


def new_id():
    return uuid4.new().hex

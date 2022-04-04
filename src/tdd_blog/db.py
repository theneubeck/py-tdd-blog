__db = {}


def clear():
    global __db
    __db = {}


def set(id, obj):
    __db[id] = obj


def delete(id):
    del __db[id]


def get(id):
    return __db.get(id)


def items():
    return __db.items()

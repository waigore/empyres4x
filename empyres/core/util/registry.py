import uuid
import weakref

Objects = weakref.WeakValueDictionary()

def register(obj):
    id = uuid.uuid4()
    Objects[id] = obj
    return id

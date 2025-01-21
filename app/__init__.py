import mongoengine as me

def connect(url):
    return me.connect(host=url)

def disconnect():
    me.disconnect()
from app import connect, disconnect
from app.functions.create import create_basic
from app.functions.read import read_basic


if __name__ == '__main__':
    db = connect('mongodb://localhost:27017/boccato_di_cardinale')

    create_basic()

    disconnect()
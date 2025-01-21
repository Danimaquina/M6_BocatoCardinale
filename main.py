from app import connect, disconnect

if __name__ == '__main__':
    db = connect('mongodb://localhost:27017/boccato_di_cardinale')

    disconnect()
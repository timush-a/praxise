from server import Server
from shelve_storage_driver import StorageDriver


HOST = '127.0.0.1'
PORT = 5000


if __name__ == '__main__':
    db = StorageDriver('lite.csv')
    db.load_storage()
    local_server = Server(HOST, PORT, db, db.select)
    local_server.run_server()

from server import Server
from json_storage_driver import Driver


HOST = '127.0.0.1'
PORT = 5000


if __name__ == '__main__':
    db = Driver('recommends.csv')
    db.load_storage()
    local_server = Server(HOST, PORT, db, db.select)
    local_server.run_server()

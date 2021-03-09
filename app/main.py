from server import Server


HOST = '127.0.0.1'
PORT = 5000


if __name__ == '__main__':
    local_server = Server(HOST, PORT)
    local_server.run_server()

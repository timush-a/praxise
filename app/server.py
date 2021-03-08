import socket
import json


class Server:
    db = None
    handler = None
    request = method = url = code = None
    sku = endpoint = probability = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def _generate_status(code: str) -> str:
        if code == 404:
            return '404 Not found'

        if code == 405:
            return '405 Method not allowed'

        return '200 OK'

    @staticmethod
    def _create_body():
        product_id = Server.sku
        probability = Server.probability
        return handler(db)

    @staticmethod
    def _generate_response():
        headers, code = Server._generate_headers()
        status = Server._generate_status(code)
        body = Server._create_body()
        if body:
            print(body)
            return f'{body}'
        return f'{headers}\n\n{status}\n\n'

    @staticmethod
    def _generate_headers() -> tuple:
        if Server.method != 'GET':
            return 'HTTP/1.1 405 Method not allowed\n\n', 405

        if Server.endpoint() != 'sku':
            return 'HTTP/1.1 404 Not found', 404

        if not Server.sku():
            return 'HTTP/1.1 404 Not found', 404

        return 'HTTP/1.1 200 OK', 200

    @staticmethod
    def __get_method() -> None:
        Server.method = Server.request.split(' ')[0]

    @staticmethod
    def __get_url() -> None:
        Server.url = Server.request.split(' ')[1]

    @staticmethod
    def __get_endpoint() -> None:
        try:
            Server.url.split('/')[1]
        except IndexError:
            pass
        Server.endpoint = Server.url.split('/')[1]

    @staticmethod
    def __get_sku(request: str):
        try:
            str(Server.url.split('/')[2])
        except (IndexError, ValueError):
            pass
        Server.sku = Server.url(request).split('/')[2]

    @staticmethod
    def __get_probability():
        try:
            0 > float(Server.url.split('/')[3]) < 1
        except (IndexError, ValueError):
            Server.probability = 0
        Server.url = Server.url.split('/')[3]

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        while True:
            client_socket, address = server_socket.accept()

            Server.request = client_socket.recv(1024).decode('utf-8')

            response = Server._generate_response()

            client_socket.sendall(response.encode())
            client_socket.close()

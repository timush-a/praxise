import socket
import storage_driver
import load_csv


class Server:
    db = load_csv.Loader.load('recommends.csv')
    handler = storage_driver.StorageDriver.select

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
    def _create_body(request: str):
        product_id = Server.__get_sku(request)
        probability = Server.__get_probability(request)
        return Server.handler(Server.db, product_id, probability)

    @staticmethod
    def _generate_response(request: str):
        headers, code = Server._generate_headers(request)
        status = Server._generate_status(code)
        body = Server._create_body(request)
        if body:
            return f'{headers}\n\n{body}'.encode()
        else:
            return f'{headers}\n\nSKU not found\n\n{status}'.encode()

    @staticmethod
    def _generate_headers(request: str) -> tuple:
        if Server.__get_method(request) != 'GET':
            return 'HTTP/1.1 405 Method not allowed\n\n', 405

        if Server.__get_endpoint(request) != 'sku':
            return 'HTTP/1.1 404 Not found', 404

        if not Server.__get_endpoint(request):
            return 'HTTP/1.1 404 Not found', 404

        return 'HTTP/1.1 200 OK', 200

    @staticmethod
    def __get_method(request: str) -> str:
        return request.split(' ')[0]

    @staticmethod
    def __get_url(request: str) -> str:
        return request.split(' ')[1]

    @staticmethod
    def __get_endpoint(request: str):
        try:
            Server.__get_url(request).split('/')[1]
        except IndexError:
            return None
        return Server.__get_url(request).split('/')[1]

    @staticmethod
    def __get_sku(request: str):
        try:
            str(Server.__get_url(request).split('/')[2])
        except (IndexError, ValueError):
            return ''
        return Server.__get_url(request).split('/')[2]

    @staticmethod
    def __get_probability(request: str) -> float:
        print(float(Server.__get_url(request).split('/')[3]))
        if 0 > float(Server.__get_url(request).split('/')[3]) > 1:
            return 1.0
        return float(Server.__get_url(request).split('/')[3])

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        while True:
            client_socket, address = server_socket.accept()

            request = client_socket.recv(1024).decode()

            response = Server._generate_response(request)

            client_socket.sendall(response)
            client_socket.close()

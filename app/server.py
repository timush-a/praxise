import socket


class Server:
    def __init__(self, host, port, database, db_select):
        self.host = host
        self.port = port
        self.storage = database
        self.db_select = db_select
        self.request = None

    def _create_body(self):
        return self.db_select(self.sku,
                              self.probability)

    def _generate_response(self) -> bytes:
        self.headers, self.code = self._generate_headers()
        self.body = self._create_body()
        if self.code != 200:
            return self.headers.encode()
        if self.body:
            return f"{self.headers}{' '.join(self.body)}".encode()

        return f'{self.headers} SKU not found'.encode()

    def _generate_headers(self) -> tuple:
        req_data = self._parse_request()
        if req_data[0] != 'GET':
            return 'HTTP/1.1 405 Method not allowed\n\n', 405

        if req_data[1] != 'get_probability':
            return 'HTTP/1.1 404 Not found\n\n', 404

        return 'HTTP/1.1 200 OK\n\n', 200

    def _parse_request(self):
        try:
            method = self.request.split(' ')[0]
            path = self.request.split(' ')[1]
            endpoint = path.split('/')[1]
        except IndexError:
            return 'Index error'

        try:
            resp_data = path.split('/')[2]
            if '&' in resp_data:
                sku = resp_data.split('&')[0]
                probability = float(resp_data.split('&')[1])
            else:
                sku = resp_data
                probability = 0
        except (IndexError, ValueError):
            sku = ''
            probability = 0

        self.sku = sku
        self.probability = probability

        return method, endpoint, sku, probability

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        while True:
            client_socket, address = server_socket.accept()

            self.request = client_socket.recv(1024).decode('utf-8')
            client_socket.send(self._generate_response())
            client_socket.close()

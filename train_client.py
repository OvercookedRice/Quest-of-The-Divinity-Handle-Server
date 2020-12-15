import socket
import json

HOST = '127.0.0.1'
PORT = 27972
BUFFER_SIZE = 4096

class TrainSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def __del__(self):
        self.sock.close()

    def connect(self):
        self.sock.connect((HOST, PORT))
        self.sock.sendall(b'/REGISTER-TRAIN-CLIENT')

        data = self.sock.recv(BUFFER_SIZE)
        print('Connection established with host: {}, port: {}'.format(HOST, PORT))

    def get_env_state(self):
        self.sock.send(b'/GET-ENV-STATE')

        data = self.sock.recv(BUFFER_SIZE)
        string_env = data.decode()

        environ = json.loads(string_env)
        return environ

conn = TrainSocket()
conn.connect()
conn.get_env_state()
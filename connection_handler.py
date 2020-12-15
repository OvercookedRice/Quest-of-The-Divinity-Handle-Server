import socket
import base64
import json

game_client_socket = None
train_socket = None

def handle_data(socket, data):
    decoded_data = data.decode()
    if decoded_data == "/REGISTER-GAME-CLIENT":
        game_client_socket = socket
        game_client_socket.send(b'/GET-ENV-STATE')

    elif decoded_data == "/REGISTER-TRAIN-CLIENT":
        train_socket = socket

    elif decoded_data.find("/ENV-STATE") != -1:
        json_data = decoded_data.split("/ENV-STATE")[1]
        game_data = json.loads(json_data)
        print(game_data)

def get_game_client_socket():
    return game_client_socket

def get_train_socket():
    return train_socket

import socket
import threading

import typer

from main_solo import *
from menus.constants import *
from menus.menu import Menu
from settings.config import SocketConfig
import sys
clients = []


def handle_client(client_socket, game_mode):
    clients.append(client_socket)
    menu = Menu(client_socket)
    while True:
        try:
            selected = menu.main_menu()
            if selected == MainMenuOption.START.value:
                if game_mode == "1":
                    play__game_ai(client_socket)
                elif game_mode == "2":
                    if len(clients) < 2:
                        client_socket.send("Waiting for another player to join...\n".encode())
                        while len(clients) < 2:
                            pass
                    play__game_player(client_socket, clients)
            elif selected == MainMenuOption.CREATE.value:
                menu.create_player_menu()
            elif selected == MainMenuOption.LEADERBOARD.value:
                menu.leaderboard_menu()
            else:
                client_socket.send("Goodbye :red_heart-emoji:".encode())
                break
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()


def main(game_mode: str):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((SocketConfig.HOST_IP, SocketConfig.HOST_PORT))
    server_socket.listen(2)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, game_mode))
        client_handler.start()


if __name__ == "__main__":
    game_mode = sys.argv[1] if len(sys.argv) > 1 else "1"
    typer.run(main)

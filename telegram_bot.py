from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, Bot
import os
import socket
from threading import Thread
import sys
from utils import get_host_ip, get_interface
import time

class Handler:
    def __init__(self, dispatcher, updater):
        self.dispatcher = dispatcher
        self.updater: Updater = updater
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        device = get_interface()
        self.server_socket.bind((get_host_ip(device), 9090))
        self.server_socket.listen()
        self.live = True
        self._ip = ""
        self.th = Thread(target=self.thread)
        self.th.setDaemon(True)
        self.th.start()

    def thread(self):
        while True:
            try:
                clientConnected, clientAddress = self.server_socket.accept()
            except OSError:
                continue
            res = clientConnected.recv(1024)
            self.ip = res.decode()
            print("Received request from", self.ip)
            context = CallbackContext(self.dispatcher)
            self.echo(context)
            time.sleep(0.5)

    def stop(self):
        self.live = False
        self.server_socket.shutdown(socket.SHUT_RDWR)
        self.server_socket.close()

    def _get_curr_dir(self):
        curr_dir = os.path.abspath(os.path.dirname(os.path.relpath(__file__)))
        return curr_dir

    def echo(self, context: CallbackContext):
        text = "Robot connected.\nIP: {}".format(self.ip)
        context.bot.send_message(chat_id="@diemturtlebotchannel", text=text)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

def main():
    global i
    updater = Updater(token=KEY)
    dispatcher = updater.dispatcher
    print("Bot started")
    handler = Handler(dispatcher, updater)
    print("Handler configurated")
    i = 0
    updater.start_polling()
    updater.idle()
    updater.stop()
    handler.stop()
    time.sleep(1)

def emergency(error):
    updater = Updater(token=KEY)
    chat_id = "268005350"
    text = "Bot disabled. Error: {}".format(error)
    bot: Bot = updater.bot
    bot.send_message(chat_id=chat_id, text=text)
    updater.stop()

if __name__ == "__main__":
    KEY = r"5379805953:AAEzJmUZrVSSQ3JjXVi-Rlbj2VUU_cOOm-A"
    channel_id = r"-1582471432"
    i = 0
    error = ""
    while i < 10:
        try:
            main()
        except Exception as e:
            print("Error!")
            print(e)
            time.sleep(30)
            i += 1
            error = e
    emergency(error)
    sys.exit(-1)

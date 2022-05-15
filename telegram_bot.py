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
        self.updater = updater
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        device = get_interface()
        self.server_socket.bind((get_host_ip(device), 9090))
        self.server_socket.listen()
        self.live = True
        self._ip = ""
        Thread(target=self.thread).start()

    def thread(self):
        while True:
            clientConnected, clientAddress = self.server_socket.accept()
            res = clientConnected.recv(1024)
            self.ip = res.decode()
            print("Received request from", self.ip)
            context = CallbackContext(self.dispatcher)
            self.echo(context)
            time.sleep(0.5)

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
    dispatcher = updater.dispatcher
    handler = Handler(dispatcher, updater)
    print("Bot started")
    i = 0
    updater.start_polling()
    updater.idle()
    updater.stop()

def emergency(error):
    global updater
    chat_id = "268005350"
    text = "Bot disabled. Error: {}".format(error)
    bot: Bot = updater.bot
    bot.send_message(chat_id=chat_id, text=text)
    updater.stop()

if __name__ == "__main__":
    KEY = r"5379805953:AAEzJmUZrVSSQ3JjXVi-Rlbj2VUU_cOOm-A"
    channel_id = r"-1582471432"
    updater = Updater(token=KEY)
    i = 0
    error = ""
    while i < 1:
        try:
            main()
        except Exception as e:
            print("Error!")
            print(e)
            time.sleep(.1)
            i += 1
            error = e
    emergency(error)
    sys.exit(-1)

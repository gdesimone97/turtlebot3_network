from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import pandas as pd
from pathlib import Path
import os
import socket
from threading import Thread
import time
from utils import get_host_ip, get_interface

class Handler:
    def __init__(self, dispatcher, updater):
        curr_dir = self._get_curr_dir()
        self.dispatcher = dispatcher
        self.updater = updater
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        device = get_interface()
        self.server_socket.bind((get_host_ip(device), 9090))
        self.server_socket.listen()
        self.live = True
        self.df_columns = ["userid"]
        self.df_path = Path(curr_dir).joinpath("users.csv")
        if not self.df_path.exists():
            self.df = pd.DataFrame(columns=self.df_columns)
            self.save_df()
        else:
            self.df = pd.read_csv(self.df_path, index_col=0)
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

    def save_df(self):
        self.df.to_csv(self.df_path)

    def start_callback(self, update: Update, context: CallbackContext):
        userid = update.effective_user.id
        data = {self.df_columns[0]: [userid]}
        self.df = pd.concat([self.df, pd.DataFrame(data)])
        self.df = self.df.drop_duplicates()
        self.save_df()

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


if __name__ == "__main__":
    KEY = r"5379805953:AAEzJmUZrVSSQ3JjXVi-Rlbj2VUU_cOOm-A"
    channel_id = r"-1582471432"
    updater = Updater(token=KEY)
    dispatcher = updater.dispatcher
    handler = Handler(dispatcher, updater)
    updater.start_polling()

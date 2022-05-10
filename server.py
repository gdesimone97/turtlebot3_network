#!/home/gdesimone/code/bash_runtime/venv/bin/python3

import netifaces as ni
import flask
from utils import get_curr_dir, get_interface
from pathlib import Path
from flask import request
import subprocess
app = flask.Flask(__name__)

@app.route("/ip")
def get_ip():
    data = request.args
    client_ip = data["client_ip"]
    path = Path(get_curr_dir(__file__)).joinpath("ssh.bash")
    text = "#!/bin/bash\n" \
           f"ssh ubuntu@{client_ip}"
    with open(str(path), "w") as fil:
        fil.write(text)
    ip = ni.ifaddresses(get_interface())[ni.AF_INET][0]['addr']
    return ip

if __name__ == "__main__":
    ip = ni.ifaddresses(get_interface())[ni.AF_INET][0]['addr']
    app.run(host=ip, port=5000)

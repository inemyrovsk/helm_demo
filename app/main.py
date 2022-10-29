import os
import socket
from flask import Flask, render_template

ENVIRONMENT = "TEST"
# ENVIRONMENT = os.getenv('DEPLOY_ENV')
# HOST = "0.0.0.0"
HOST = os.getenv('HOST')
# PORT = 8000
PORT_STR = os.getenv('PORT')
PORT = int(PORT_STR)

app = Flask(ENVIRONMENT)


@app.route("/")
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    with open('/mnt/.secret', 'r') as secret:
        secret_str, secret_str1, secret_str2 = [x for x in secret.readlines()]
    with open('/mnt/.super-secret', 'r') as super_secret:
        super_secret_str, super_secret_str1 = [x for x in super_secret.readlines()]
    return render_template(
        'index.html', ip_addr=ip_address, hostname=hostname, secret_string=secret_str,
        secret_str1=secret_str1, secret_str2=secret_str2,
        super_secret_str=super_secret_str,
        super_secret_str1=super_secret_str1
    )


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)

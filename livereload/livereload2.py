# -*- encoding: utf-8 -*-
from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)


if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

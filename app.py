#!flask/bin/python3
# -*- coding: utf-8 -*-

from src import app

DEBUG = True

app.run(
        debug=DEBUG,
        host='0.0.0.0',
        threaded=True
    )
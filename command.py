#!/usr/bin/python
from __future__ import unicode_literals, print_function, absolute_import

import gevent.monkey
gevent.monkey.patch_all()
import psycogreen.gevent
psycogreen.gevent.patch_psycopg()

import application
import logging
import os
import os.path
import json
import argparse
import gevent.wsgi

app = application.app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')

    folder = os.path.dirname(__file__)
    fc = os.path.join(folder, "config.json")
    with open(fc, "rb") as file_:
        fc_content = file_.read().decode("utf8")
    config = json.loads(fc_content)
    app.configure(config)

    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(dest='action')

    parser_serve = subparsers.add_parser('serve', help='serves in development mode')
    parser_serve.add_argument('-p', '--port', type=int, default=5000)
    parser_serve.add_argument('-o', '--host', default="localhost")
    def serve():
        server = gevent.wsgi.WSGIServer((args.host, args.port), app.web_app)
        server.serve_forever()
    parser_serve.set_defaults(func=serve)

    parser_createdb = subparsers.add_parser('createdb', help='creates the database according to configuration')
    parser_createdb.add_argument('-d', '--dev', action="store_true", default=False)
    def createdb():
        with app:
            app.create_tables()
    parser_createdb.set_defaults(func=createdb)

    args = parser.parse_args()
    args.func()

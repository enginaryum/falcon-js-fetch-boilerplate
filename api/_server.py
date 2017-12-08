# -*- coding: utf-8 -*-
from wsgiref import simple_server
from middleware import public_cors, JSONTranslator
from resources import HelloWorldResource
import falcon

wsgi_app = api = falcon.API(middleware=[public_cors.middleware, JSONTranslator()], )

helloWorld = HelloWorldResource()

api.add_route('/api/hello', helloWorld)
httpd = simple_server.make_server('127.0.0.1', 8765, api)
httpd.serve_forever()

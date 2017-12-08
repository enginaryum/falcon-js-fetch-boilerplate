# -*- coding: utf-8 -*-
import falcon


class HelloWorldResource(object):

  def on_get(self, req, res):
    result = {"message": "Hello World!"}
    req.context['result'] = result
    res.status = falcon.HTTP_200


# -*- coding: utf-8 -*-
import falcon, json
from falcon_cors import CORS

public_cors = CORS(
  allow_all_origins=True,
  allow_all_methods=True,
  allow_all_headers=True,
  allow_credentials_all_origins=True
)


class RequireJSON(object):
  def process_request(self, req, resp):
    if not req.client_accepts_json:
      raise falcon.HTTPNotAcceptable(
        'This API only supports responses encoded as JSON.',
        href='http://docs.examples.com/api/json'
      )

    if req.method in ('POST', 'PUT'):
      if 'application/json' not in req.content_type:
        raise falcon.HTTPUnsupportedMediaType(
          'This API only supports requests encoded as JSON.',
          href='http://docs.examples.com/api/json'
        )


class JSONTranslator(object):
  def process_request(self, req, resp):
    if req.content_length in (None, 0):
      return

    body = req.stream.read()
    if not body:
      raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')

    try:
      req.body = json.loads(body.decode('utf-8'))

    except (ValueError, UnicodeDecodeError):
      raise falcon.HTTPError(
        falcon.HTTP_753,
        'Malformed JSON',
        'Could not decode the request body. The JSON was incorrect or not encoded as UTF-8.')

  def process_response(self, req, resp, resource):
    resp.content_type = 'application/json'
    if 'result' not in req.context:
      return
    try:
      req.context['success']
    except KeyError:
      req.context['result']['success'] = True
    resp.body = json.dumps(req.context['result'])

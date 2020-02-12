
import sys
import logging
from helpr.http_exceptions import HTTPExceptions


class ServiceHandler():
  INTEGER = 0
  FLOAT = 1
  STRING = 2
  BOOLEAN = 3
  LIST = 4
  TYPE_MAP = [int, float, str, bool, list]

  def __init__(self, endpoint, method, rqparams=None, rbparams=None, rpparams=None):
    """
    Init Handler Object
    :param endpoint: http resource/endpoint
    :param method: http method
    :param rqparams: required query params
    :param rbparams: required body params
    :param rpparams: required path params
    :type endpoint: string
    :type method: string
    :type rqparams: dict 
    :type rbparams: dict 
    :type rpparams: dict
    """

    if type(endpoint) != str:
      raise ValueError('Parameter code: Type Error (It should be string)')

    if type(method) != str:
      raise ValueError('Parameter method: Type Error (It should be string)')

    if type(rpparams) != dict and rpparams != None:
      raise ValueError('Parameter rpparams: Type Error (It should be dictionary)')
    
    if type(rqparams) != dict and rqparams != None:
      raise ValueError('Parameter rqparams: Type Error (It should be dictionary)')

    if type(rbparams) != dict and rbparams != None:
      raise ValueError('Parameter rbparams: Type Error (It should be dictionary)')


    self.rpparams = rpparams
    self.endpoint = endpoint
    self.method = method
    self.rqparams = rqparams
    self.rbparams = rbparams


  @staticmethod
  def __recursive_attrb_check(endpoint, params, required_params):
    for rp in required_params.keys():
      if rp not in params:
        HTTPExceptions.raise_exception(
          HTTPExceptions.BAD_REQUEST,
          endpoint,
          rp
        )
      else:
        if type(required_params[rp]) == dict:
          if type(params[rp]) != dict:
            HTTPExceptions.raise_exception(
              HTTPExceptions.BAD_REQUEST,
              endpoint,
              rp
            )
          else:
            ServiceHandler.__recursive_attrb_check(
              endpoint,
              params[rp],
              required_params[rp]
            )
        else:
          if type(params[rp]) != ServiceHandler.TYPE_MAP[required_params[rp]]:
            HTTPExceptions.raise_exception(
              HTTPExceptions.BAD_REQUEST,
              endpoint,
              rp
            )


  def _validate_request_params(self, qparams=None, reqbody=None, path_params=None):
    """
    :param qparams: query param
    :param reqbody: request body
    :type qparams: dict
    :type reqbody: dict
    :type path_params: dict
    """
    if type(qparams) != dict and qparams != None:
      raise ValueError('Param qparams: Type Error (It shoud be dicitonary)')

    if type(reqbody) != dict and reqbody != None:
      raise ValueError('Param reqbody: Type Error (It shoud be dicitonary)')

    if type(path_params) != dict and path_params != None:
      raise ValueError('Param reqbody: Type Error (It shoud be dicitonary)')

    if self.rpparams:
      if path_params == None:
        HTTPExceptions.raise_exception(
          HTTPExceptions.BAD_REQUEST,
          self.endpoint,
          '( Empty Param )'
        )
      ServiceHandler.__recursive_attrb_check(self.endpoint, path_params, self.rpparams)

    if self.rqparams:
      if qparams == None:
        HTTPExceptions.raise_exception(
          HTTPExceptions.BAD_REQUEST,
          self.endpoint,
          '( Empty Param )'
        )
      ServiceHandler.__recursive_attrb_check(self.endpoint, qparams, self.rqparams)


    if self.rbparams:
      if reqbody == None:
        HTTPExceptions.raise_exception(
          HTTPExceptions.BAD_REQUEST,
          self.endpoint,
          '( Empty Param )'
        )
      ServiceHandler.__recursive_attrb_check(self.endpoint, reqbody, self.rbparams)

    return 0







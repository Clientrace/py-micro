
import sys
import logging
from helpr.http_exceptions import *

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class ServiceHandler():

  def __init__(self, endpoint, method, rqparams, rbparams):
    """
    Init Handler Object
    :param endpoint: http resource/endpoint
    :param method: http method
    :param rqparams: required query params
    :param rbparams: required body params
    :type endpoint: string
    :type method: string
    :type rqparams: list
    :type rbparams: list
    """

    if type(endpoint) != str:
      raise ValueError('Parameter code: Type Error (It should be string)')

    if type(method) != str:
      raise ValueError('Parameter method: Type Error (It should be string)')
    
    if type(rqparams) != list and rqparams != None:
      raise ValueError('Parameter rqparams: Type Error (It should be list)')

    if type(rbparams) != list and rbparams != None:
      raise ValueError('Parameter rbparams: Type Error (It should be list)')

    self.endpoint = endpoint
    self.method = method
    self.rqparams = rqparams
    self.rbparams = rbparams

  def _validate_request_params(self, qparams, reqbody=None):
    """
    :param qparams: query param
    :param reqbody: request body
    :type qparams: dict
    :type reqbody: dict
    """
    if type(qparams) != dict and qparams != None:
      raise ValueError('Param qparams: Type Error (It shoud be dicitonary)')

    if type(reqbody) != dict and reqbody != None:
      raise ValueError('Param reqbody: Type Error (It shoud be dicitonary)')

    if self.rqparams:
      if qparams == None:
        HTTPExceptions.raise_exception(
          HTTPExceptions.BAD_REQUEST,
          self.endpoint,
          '( Empty Param )'
        )

      for param in self.rqparams:
        if param not in qparams:
          HTTPExceptions.raise_exception(
            HTTPExceptions.BAD_REQUEST,
            self.endpoint,
            param
          )

    if self.method == 'post':
      if self.rbparams:
        if reqbody == None:
          HTTPExceptions.raise_exception(
            HTTPExceptions.BAD_REQUEST,
            self.endpoint,
            '( Empty Param )'
          )

        for param in self.rbparams:
          if param not in reqbody:
            HTTPExceptions.raise_exception(
              HTTPExceptions.BAD_REQUEST,
              self.endpoint,
              param
            )
    return 0







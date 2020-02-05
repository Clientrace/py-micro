
import logging
from helpr.http_exceptions import HTTPExceptions      


class ServiceHandler():

  def __init__(self, endpoint, method, qparams, rparams):
    """
    Init Handler Object
    :param endpoint: http resource/endpoint
    :param method: http method
    :param qparams: query params
    :param rparams: required params
    :type endpoint: string
    :type method: string
    :type qparams: dictionary
    :type rparams: dictionary
    """

    if type(endpoint) != str:
      raise ValueError('Parameter code: Type Error (It should be string)')

    if type(method) != str:
      raise ValueError('Parameter code: Type Error (It should be string)')
    
    if type(qparams) != dict:
      raise ValueError('Parameter code: Type Error (It should be dictionary)')

    if type(rparams) != list:
      raise ValueError('Parameter code: Type Error (It should be list)')

    self.endpoint = endpoint
    self.method = method
    self.qparams = qparams
    self.rparams = rparams

  def _validate_request_params(self):

    if self.method.lower() == 'get':
      for param in self.rparams:
        if param not in self.qparams.keys():
          HTTPExceptions.raise_exception(
            HTTPExceptions.BAD_REQUEST,
            self.endpoint
          )

    # if method.lower() == 'post':
    #   pass





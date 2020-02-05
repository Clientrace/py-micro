      
class Handler():

  def __init__(self, endpoint, method, qparams, rparams):
    """
    Init Handler Object
    :param method: http method
    :param qparams: query params
    :param rparams: required params
    :type method: string
    :type qparams: dictionary
    :type rparams: dictionary
    """
    self.endpoint = endpoint
    self.method = method
    self.qparams = qparams
    self.rparams = rparams

  @staticmethod
  def _validate_request_params(endpoint, method, qparams, rparams):

    if method.lower() == 'get':
      for param in rparams:
        if param not in rparams:
          HTTPExceptions.raise_exception(
            HTTPExceptions.BAD_REQUEST,
            endpoint
          )

    if method.lower() == 'post':
      pass





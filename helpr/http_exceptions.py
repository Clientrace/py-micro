
class Error(Exception):
  """
  Base Class for Exceptions
  """
  pass

class BadRequest(Error):
  """
  Status Code 400
  """
  def __init__(self, code, msg, endpoint):
    if type(code) != int:
      raise ValueError('Parameter code: Type Error (It should be integer)')

    if type(msg) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    if type(endpoint) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    self.code = code
    self.msg = msg
    self.endpoint = endpoint

class InternalServerError(Error):
  """
  Status Code 500
  """
  def __init__(self, code, msg, endpoint):
    if type(code) != int:
      raise ValueError('Parameter code: Type Error (It should be integer)')

    if type(msg) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    if type(endpoint) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    self.code = code
    self.msg = msg
    self.endpoint = endpoint


class HTTPExceptions:

  INTERNAL_SERVER_ERROR = 500
  METHOD_NOT_ALLOWED = 405
  NOT_FOUND = 404
  BAD_REQUEST = 400

  @staticmethod
  def raise_exception(statusCode, endpoint):
    """
    Raise HTTP Exception
    :param statusCode: HTTP Status Code
    :param endpoint: API Endpoint/Resource
    :type statusCode: integer
    :type endpoint: string
    """

    if statusCode == HTTPExceptions.BAD_REQUEST:
      raise BadRequest(
        statusCode,
        'Bad Request',
        endpoint)

    if statusCode == HTTPExceptions.INTERNAL_SERVER_ERROR:
      raise InternalServerError(
        statusCode,
        'Internal Server Error',
        endpoint
      )




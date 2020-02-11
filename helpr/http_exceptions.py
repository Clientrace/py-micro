
class Error(Exception):
  """
  Base Class for Exceptions
  """
  pass

class BadRequest(Error):
  """
  Status Code 400
  """
  def __init__(self, code, msg, endpoint, fieldError):
    if type(code) != int:
      raise ValueError('Parameter code: Type Error (It should be integer)')

    if type(msg) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    if type(endpoint) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    if type(fieldError) != str:
      raise ValueError('Parameter msg: Type Error (It should be string)')

    self.code = code
    self.msg = msg
    self.endpoint = endpoint
    self.fieldError = fieldError

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
      raise ValueError('Parameter endpint: Type Error (It should be string)')

    self.code = code
    self.msg = msg
    self.endpoint = endpoint

class MethodNotAllowed(Error):
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
  BAD_REQUEST = 400

  @staticmethod
  def raise_exception(statusCode, endpoint, field=None):
    """
    Raise HTTP Exception
    :param statusCode: HTTP Status Code
    :param endpoint: API Endpoint/Resource
    :param field: Missing Field for Bad Request
    :type statusCode: integer
    :type endpoint: string
    """

    if statusCode == HTTPExceptions.BAD_REQUEST:
      raise BadRequest(
        HTTPExceptions.BAD_REQUEST,
        'Bad Request',
        endpoint,
        field
      )

    if statusCode == HTTPExceptions.INTERNAL_SERVER_ERROR:
      raise InternalServerError(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        'Internal Server Error',
        endpoint
      )

    if statusCode == HTTPExceptions.METHOD_NOT_ALLOWED:
      raise MethodNotAllowed(
        HTTPExceptions.METHOD_NOT_ALLOWED,
        'Method not Allowed',
        endpoint
      )







from helpr.service_handler import ServiceHandler


class AWSServiceHandler:

  INTEGER = 0
  FLOAT = 1
  STRING = 2
  BOOLEAN = 3
  LIST = 4
  TYPE_MAP = [int, float, str, bool, list] 

  def __init__(self, event, rqparams, rbparams):
    print(event)
    self.path = event['requestContext']['resourcePath']
    self.httpMethod = event['httpMethod']
    self.pathParams = event['pathParameters']
    self.queryStringParams = event['queryStringParameters`']
    self.eventBody = event['body']
    self.service_handler = ServiceHandler(
      self.path,
      self.httpMethod,
      rqparams,
      rbparams
    )

  def validate_request_params(self):
    print(self.pathParams)
    print(self.eventBody)
    print(type(self.pathParams))
    print(type(self.eventBody))

    self.service_handler._validate_request_params(
      self.pathParams,
      self.eventBody
    )


  def get_request_params(self):
    return self.pathParams


  def get_request_body(self):
    return self.eventBody







import json
from helpr.service_handler import ServiceHandler
from helpr.http_exceptions import *


class AWSServiceHandler:

  INTEGER = 0
  FLOAT = 1
  STRING = 2
  BOOLEAN = 3
  LIST = 4
  TYPE_MAP = [int, float, str, bool, list] 

  def __init__(self,
     event,
     Repo,
     Service,
     ReqQueryparams=None,
     ReqBody=None,
     ReqPathParams=None):

    self.path = event['requestContext']['resourcePath']
    self.httpMethod = event['httpMethod']
    self.pathParams = event['pathParameters']
    self.queryStringParams = event['queryStringParameters']
    self.eventBody = json.loads(event['body'])

    self.service_handler = ServiceHandler(
      endpoint = self.path,
      method = self.httpMethod,
      rqparams = ReqQueryparams,
      rbparams = ReqBody,
      rpparams = ReqPathParams
    )


    print('===================')
    print(self.queryStringParams)
    print(self.eventBody)
    print(self.pathParams)
    print('===================')

    self.service = Service(
      Repo,
      self.queryStringParams,
      self.eventBody,
      self.pathParams
    )

  def execute(self):
    # Raise Error Upon Validation
    self.service_handler._validate_request_params(
      qparams = self.queryStringParams,
      reqbody = self.eventBody,
      path_params = self.pathParams
    )

    # Run Service
    try:
      resp = self.service.execute()
    except Exception as e:
      print(str(e))
      HTTPExceptions.raise_exception(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        self.path,
        'Server Error'
      )

    return resp



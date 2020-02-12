
import json
from helpr.service_handler import ServiceHandler
from helpr.http_exceptions import *


class AWSServiceHandler:
  """
  Service Handler for AWS Events with field type validations
  INTEGER - for integer type fields
  FLOAT - floating type fields
  STRING - string type fields
  BOOLEAN - boolean type fields
  LIST - array type fields
  """

  INTEGER = 0
  FLOAT = 1
  STRING = 2
  BOOLEAN = 3
  LIST = 4

  def __init__(self,
     event,
     Repo,
     Service,
     ReqQueryParams=None,
     ReqBody=None,
     ReqPathParams=None):
    """
    Initialize Service Handler for AWS
    :param event: AWS Event
    :param Repo: repository
    :param Service: service use case
    :param ReqQueryParams: Required Query String Params
    :param ReqBody: Required Request Body
    :param ReqpathParams: Required Path Parameters
    :type event: dictionary
    :type Repo: Repository object
    :type Service: Service Object
    :yype ReqQueryParams: dictionary
    :type ReqBody: dictionary
    :type ReqPathParams: dictionary
    """

    # Parse aws event and get the httpmethod, pathParams, querystring params,
    # and query request body for post
    self.path = event['requestContext']['resourcePath']
    self.httpMethod = event['httpMethod']
    self.pathParams = event['pathParameters']
    self.queryStringParams = event['queryStringParameters']
    self.eventBody = json.loads(event['body'])

    # Initialize Service Handler for the request
    self.service_handler = ServiceHandler(
      endpoint = self.path,
      method = self.httpMethod,
      rqparams = ReqQueryParams,
      rbparams = ReqBody,
      rpparams = ReqPathParams
    )

    # Initialize the service for the request
    self.service = Service(
      Repo,
      self.queryStringParams,
      self.eventBody,
      self.pathParams
    )

  def execute(self):
    """
    Execute Service Request
    :returns: request status and body
    :rtype: dictionary
    """
    # Raise Error Upon Validation
    self.service_handler._validate_request_params(
      qparams = self.queryStringParams,
      reqbody = self.eventBody,
      path_params = self.pathParams
    )

    # Execute the service
    try:
      resp = self.service.execute()
    except Exception as e:
      HTTPExceptions.raise_exception(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        self.path,
        'Server Error'
      )

    return resp






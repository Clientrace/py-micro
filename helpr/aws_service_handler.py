
import sys
import json
import logging
import traceback
from helpr import http_exceptions
from helpr.service_handler import ServiceHandler
from helpr.http_exceptions import HTTPExceptions

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

    # Set Logger
    logging.getLogger().setLevel(logging.INFO)

    # Parse aws event and get the httpmethod, pathParams, querystring params,
    # and query request body for post
    self.path = event['requestContext']['resourcePath']
    self.httpMethod = event['httpMethod'].lower()
    self.pathParams = event['pathParameters']
    self.queryStringParams = event['queryStringParameters']
    self.eventBody = AWSServiceHandler.parse_json(event['body'])

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

  @classmethod
  def parse_json(cls, jsonstring):
    ret = None
    try:
      return json.loads(jsonstring)
    except Exception:
      ret = {}
    return ret

  def execute(self):
    """
    Execute Service Request
    :returns: request status and body
    :rtype: dictionary
    """

    # Raise Error Upon Validation
    try:
      self.service_handler._validate_request_params(
        qparams = self.queryStringParams,
        reqbody = self.eventBody,
        path_params = self.pathParams
      )
    except Exception as e:
      logging.info(' ' + self.path + ' ' + self.httpMethod + ' - ' + str(e.args[0]))
      return {
        'statusCode' : e.args[0],
        'body' : str(e.args)
      }

    # Execute the service
    try:
      resp = self.service.execute()
    except (http_exceptions.BadRequest, http_exceptions.InternalServerError, \
      http_exceptions.MethodNotAllowed): 
      logging.info(' ' + self.path + ' ' + self.httpMethod + ' - ' + str(e.args[0]))
      return {
        'statusCode' : e.args[0],
        'body' : str(e.args)
      }
    except Exception as e:
      logging.info(' ' + self.path + ' ' + self.httpMethod + ' - 500 INTERNAL SERVER ERROR')
      exc_info = sys.exc_info()
      traceback.print_exception(*exc_info)

      HTTPExceptions.raise_exception(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        self.path,
        'Server Error'
      )

    logging.info(' ' + self.path + ' ' + self.httpMethod + ' - ' + str(resp['statusCode']))

    return resp



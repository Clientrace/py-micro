
from helpr.service_handler import ServiceHandler


class AWSServiceHandler:
  def __init__(self, event, rqparams, rbparams):
    self.path = event['requestContext']['resourcePath']
    self.httpMethod = event['httpMethod']
    self.pathParams = event['pathParameters']
    self.evenBody = event['body']
    self.service_handler = ServiceHandler(
      self.path,
      self.httpMethod,
      rqparams,
      rbparams
    )

  def validate_request_params(self):
    self.service_handler._validate_request_params(
      self.pathParams,
      self.evenBody
    )








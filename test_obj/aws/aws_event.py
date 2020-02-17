import json

class AWSMockEvent:
  """
  AWS Mock event object for testing endpoints
  """

  def __init__(self, ResourcePath, HTTPMethod, PathParam=None, PathParams=None, 
    QueryStringParams=None, RequestBody=None):
    """
    Create Event Payload
    :param event: AWS Event
    :param Repo: repository
    :param Service: service use case
    :param QueryParams: Query String Params
    :param ReqBody: Request Body
    :param PathParams: Path Parameters
    :type event: dictionary
    :type Repo: Repository object
    :type Service: Service Object
    :yype ReqQueryParams: dictionary
    :type ReqBody: dictionary
    :type ReqPathParams: dictionary
    """

    self.eventPayload = {
      'requestContext' : {
        'resourcePath' : ResourcePath
      },
      'httpMethod' : HTTPMethod,
      'pathParameters' : PathParams,
      'queryStringParameters' : QueryStringParams,
      'body' : json.dumps(RequestBody)
    }

  def get_event(self):
    """
    Get Event Payload
    """
    return self.eventPayload





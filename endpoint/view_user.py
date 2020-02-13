
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.view_user import ViewUser
from ms import dynamodb_repo

def handler(event, context):
  """
  @api {get} /user/view/{id}
  @apiName Create User
  @apiGroup User

  @apiDescription View Specific User

  @apiSuccessExample Success-Response:
  HTTP/1.1 200 OK
  {
    "id" : <generated id>,
    "name" : <user's name>,
    "address" : <user's address>,
    "age" : "<user's age>
  }
  """

  svh = AWSServiceHandler(
    event,
    Service = ViewUser,
    Repo=dynamodb_repo.DynamoDBRepo(
      'users_table',
      'ap-southeast-1'
    ),
    ReqPathParams={
      'id' : AWSServiceHandler.STRING
    }
  )

  return svh.execute()


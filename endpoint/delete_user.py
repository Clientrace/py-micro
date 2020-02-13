
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.delete_user import DeleteUser
from ms import dynamodb_repo

def handler(event, context):
  """
  @api {get} /user/delete/{id}
  @apiName Delete
  @apiGroup User

  @apiDescription Delete User by ID

  @apiSuccessExample Success-Response:
  HTTP/1.1 200 OK
  {}
  """
  svh = AWSServiceHandler(
    event,
    Service = DeleteUser,
    Repo=dynamodb_repo.DynamoDBRepo(
      'users_table',
      'ap-southeast-1'
    ),
    ReqPathParams={
      'id' : AWSServiceHandler.STRING
    }
  )

  return svh.execute()

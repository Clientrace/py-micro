
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.update_user import UpdateUser
from ms import dynamodb_repo

def handler(event, context):
  """
  @api {put} /user/create/
  @apiName Update User
  @apiGroup User

  @apiDescription Update User Fields

  @apiParam {String} name user's name
  @apiParam {String} address user's address
  @apiParam {Integer} age user's age

  @apiSuccessExample Success-Response:
  HTTP/1.1 200 OK
  {}
  """

  svh = AWSServiceHandler(
    event,
    Service = UpdateUser,
    Repo=dynamodb_repo.DynamoDBRepo(
      'users_table',
      'ap-southeast-1'
    ),
    ReqPathParams={
      'id' : AWSServiceHandler.STRING
    }
  )

  return svh.execute()


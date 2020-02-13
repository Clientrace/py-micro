
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.create_user import CreateUser
from ms import dynamodb_repo

def handler(event, context):
  """
  @api {post} /user/create/
  @apiName Create User
  @apiGroup User

  @apiDescription Create a user

  @apiParam {String} name user's name
  @apiParam {String} address user's address
  @apiParam {Integer} age user's age

  @apiSuccessExample Success-Response:
  HTTP/1.1 200 OK
  {
    "id" : <generated id>
  }
  """

  svh = AWSServiceHandler(
    event,
    Service = CreateUser,
    Repo=dynamodb_repo.DynamoDBRepo(
      'users_table',
      'ap-southeast-1'
    ),
    ReqBody={
      'name' : AWSServiceHandler.STRING,
      'address' : AWSServiceHandler.STRING,
      'age' : AWSServiceHandler.INTEGER
    }
  )

  return svh.execute()




